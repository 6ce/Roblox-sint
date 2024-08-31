import requests
import time

class Snusbase:
    """A module for interacting with the https://niggerbase.xyz API"""
    def __init__(self):
        self._lookupUrl = "https://niggerbase.xyz/lookup"
        self._headers = {"Content-Type": "application/json"}
        self._validQueryTypes = ["username", "name", "lastip", "email", "password", "hash", "domain"]

    def _isValidQueryType(self, queryType: str) -> bool:
        """Returns whether or not the input queryType is valid"""
        return queryType.lower() in self._validQueryTypes

    def search(self, query: str, queryType="username") -> list[dict]:
        """Performs a search on the input query of queryType on Snusbase"""
        if not self._isValidQueryType(queryType):
            raise Exception("Invalid query type passed")
        
        try:
            data = {queryType: query}
            start = time.time()

            response = requests.post(self._lookupUrl, headers=self._headers, json=data)
            results = response.json()

            elapsed = round(time.time() - start, 2)
            elapsedText = f"{elapsed}s"

            return {
                "success": True, 
                "query": query, 
                "type": queryType, 
                "took": elapsedText, 
                "data": results
            }
        except Exception as err:
            return {
                "success": False, 
                "query": query, 
                "type": queryType, 
                "errors": [err]
            }
    
    def usernameSearch(self, username: str) -> list[dict]:
        """Performs a username search on Snusbase"""
        return self.search(username, "username")
    
    def nameSearch(self, name: str) -> list[dict]:
        """Performs a name search on Snusbase"""
        return self.search(name, "name")
    
    def ipSearch(self, ip: str) -> list[dict]:
        """Performs an IP address search on Snusbase"""
        return self.search(ip, "lastip")
    
    def emailSearch(self, email: str) -> list[dict]:
        """Performs an email search on Snusbase"""
        return self.search(email, "email")
    
    def passwordSearch(self, password: str) -> list[dict]:
        """Performs a password search on Snusbase"""
        return self.search(password, "password")
    
    def hashSearch(self, hash: str) -> list[dict]:
        """Performs a hash search on Snusbase"""
        return self.search(hash, "hash")
    
    def domainSearch(self, domain: str) -> list[dict]:
        """Performs a domain search on Snusbase"""
        return self.search(domain, "domain")
