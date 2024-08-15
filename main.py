import json
import sys
import time
import snusbase
from cavalier import Cavalier
from roblox import Roblox

TIME_PER_SEARCH = 1.5 * 2 # time per search (both cavalier and snusbase)

def main(userId: int):
    results = ""

    cavalier = Cavalier()
    roblox = Roblox()

    usernames = roblox.getPastUsernames(userId)
    if usernames[0] == "User not found":
        return exit("User not found")

    estimated = len(usernames) * TIME_PER_SEARCH
    print("Searching for usernames: {}".format(str(usernames)))
    print("Estimated search time: {} seconds".format(str(estimated)))

    for user in usernames:
        print("Doing cavalier search for '{}'".format(user))
        result = cavalier.usernameSearch(user)
        _result = json.dumps(result, indent=4)
        results += f"Cavalier results for: '{user}':\n{_result}\n"

        print("Doing Snusbase search for '{}'".format(user))
        result2 = snusbase.search(user, "username")
        if result2["success"]:
            _result2 = json.dumps(result2["data"], indent=4)
            results += f"Snusbase results for: '{user}':\n{_result2}\n\n"
        else:
            results += f"Failed to search {user} with Snusbase: {result2["errors"]}\n\n"

        time.sleep(0.5)

    with open("result.txt", "w") as file:
        file.write(results)
    
    print("Check 'result.txt' for search results")

if len(sys.argv) < 2:
    print("Usage: python main.py [userId]")
    exit("Example Usage: python main.py 123")

userId = sys.argv[1]
main(userId)
