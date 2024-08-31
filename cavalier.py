import requests

class Cavalier:
    """A module for interacting with the https://cavalier.hudsonrock.com API"""
    def __init__(self):
        self.api = "https://cavalier.hudsonrock.com/api/json/v2"

    def _search(self, path: str) -> list:
        """Performs a get request to the input API path on https://cavalier.hudsonrock.com"""
        url = self.api + path
        response = requests.get(url)
        try:
            data = response.json()
            return data["stealers"]
        except:
            return []

    def usernameSearch(self, username: str) -> list:
        """Performs a username search on https://cavalier.hudsonrock.com"""
        path = "/osint-tools/search-by-username?username={}".format(username)
        return self._search(path)
    
    def emailSearch(self, email: str) -> list:
        """Performs an email search on https://cavalier.hudsonrock.com"""
        path = "/osint-tools/search-by-email?email={}".format(email)
        return self._search(path)
    
    def ipSearch(self, ip: str) -> list:
        """Performs an IP address search on https://cavalier.hudsonrock.com"""
        path = "/osint-tools/search-by-ip?ip={}".format(ip)
        return self._search(path)
