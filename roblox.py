import requests

class Roblox:
    """A module for interacting with the https://roblox.com API"""
    def __init__(self):
        self.api = "https://users.roblox.com/v1"

    def _removeDupes(self, lst: list) -> list:
        """Removes duplicate items from a list"""
        return list(set(lst))

    def _get(self, path: str) -> requests.Response:
        """Performs a get request to the input API path on https://roblox.com"""
        url = self.api + path
        return requests.get(url)
    
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
