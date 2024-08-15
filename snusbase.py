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
        return queryType.lower() in self.validQueryTypes

    def search(self, query: str, queryType="username") -> list[dict]:
        """Performs a search on the input query of queryType"""
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
