# TODO: implement unique-ness functionality (force only unique usernames to be returned)

import requests

class Roblox:
    """A module for interacting with the https://roblox.com API"""
    def __init__(self):
        self.api = "https://users.roblox.com/v1"

    """Performs a get request to the input API path on https://roblox.com"""
    def _get(self, path: str) -> requests.Response:
        url = self.api + path
        return requests.get(url)
    
    """Get's the input userId's username"""
    def getUsername(self, userId: int) -> str:
        id = str(userId)
        path = "/users/{}".format(id)
        response = self._get(path)

        try:
            data: dict = response.json()
            return data["name"]
        except:
            return "User not found"

    """Get's the input userId's list of past usernames (and current)"""
    def getPastUsernames(self, userId: int) -> list[str]:
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
            return users
        except:
            return ["No past usernames"]
