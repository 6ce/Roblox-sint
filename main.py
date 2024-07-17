# TODO: implement a snusbase searching functionality

import json
import sys
import time
from cavalier import Cavalier
from roblox import Roblox

TIME_PER_CAVALIER_SEARCH = 1.5 # time per cavalier search (for estimating total time)

def main(userId: int):
    results = ""

    cavalier = Cavalier()
    roblox = Roblox()

    usernames = roblox.getPastUsernames(userId)
    if usernames[0] == "User not found":
        return exit("User not found")

    estimated = str(len(usernames) * TIME_PER_CAVALIER_SEARCH)
    print("Searching for usernames: {}".format(str(usernames)))
    print("Estimated search time: {} seconds".format(estimated))

    for user in usernames:
        print("Doing cavalier search for '{}'".format(user))
        result = cavalier.usernameSearch(user)
        _result = json.dumps(result, indent=4)
        results += f"Cavalier results for: '{user}':\n{_result}\n\n"
        time.sleep(0.5)

    with open("result.txt", "w") as file:
        file.write(results)
    
    print("Check 'result.txt' for search results")

if len(sys.argv) < 2:
    print("Usage: python main.py [userId]")
    exit("Example Usage: python main.py 123")

userId = sys.argv[1]
main(userId)
