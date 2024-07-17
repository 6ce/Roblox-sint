import requests

class Cavalier:
    """A module for interacting with the https://cavalier.hudsonrock.com API"""
    def __init__(self):
        self.api = "https://cavalier.hudsonrock.com/api/json/v2"

    """Performs a get request to the input api path on https://cavalier.hudsonrock.com"""
    def _get(self, path: str) -> requests.Response:
        url = self.api + path
        return requests.get(url)

    """Performs a username search on https://cavalier.hudsonrock.com"""
    def usernameSearch(self, username: str) -> list | str:
        path = "/osint-tools/search-by-username?username={}".format(username)
        response = self._get(path)
        
        try:
            data = response.json()
            return data["stealers"]
        except:
            return response.text
