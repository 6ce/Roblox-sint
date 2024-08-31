import requests

class Roblox:
    """A module for interacting with the https://roblox.com API"""
    def __init__(self):
        self.api = "https://users.roblox.com/v1"

    def _removeDupes(self, lst: list) -> list:
        """Removes duplicate items from a list"""
        return list(set(lst))

    def _get(self, path: str) -> requests.Response:
        """Performs a GET request to the input API path on https://users.roblox.com"""
        url = self.api + path
        return requests.get(url)
    
    def _post(self, path: str, data: dict) -> requests.Response:
        """Performs a POST request to the input API path on https://users.roblox.com"""
        url = self.api + path
        headers = {"Content-Type": "application/json"}
        return requests.post(url, headers=headers, json=data)
    
    def getUserId(self, username: str) -> int:
        """Get's the input username's userId"""
        path = "/usernames/users"
        data = {"usernames": [username], "excludeBannedUsers": False}
        response = self._post(path, data)
        
        try:
            data: list = response.json()["data"]
            return data[0]["id"]
        except:
            return "User not found"
    
    def getUsername(self, userId: int) -> str:
        """Get's the input userId's username"""
        id = str(userId)
        path = "/users/{}".format(id)
        response = self._get(path)

        try:
            data: dict = response.json()
            return data["name"]
        except:
            return "User not found"

    def getPastUsernames(self, userId: int) -> list[str]:
        """Get's the input userId's list of past usernames, then appends the current username to the list"""
        currentUser = self.getUsername(userId)
        if currentUser == "User not found":
            return ["User not found"]

        id = str(userId)
        path = "/users/{}/username-history?limit=100".format(id)
        response = self._get(path)
        
        try:
            data: dict = response.json()
            users = [name["name"] for name in data["data"]]
            users.append(currentUser)
            return self._removeDupes(users)
        except Exception as e:
            return [currentUser]
