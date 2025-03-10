# This is an app that generates a basic pokemon team for you and allows you to delete and add new pokemon at will.

# Prompt user about program DONE
# Access database of pokemn DONE
# display available pokemon to user DONE

# Update initial display to show pokemon as a list

# prompt use to add pokemon (select from list?)

import poke_db.server_query as server_query

print("WELCOME TO POKEGEN")

userReq = int(input("TYPE '1' if you'd like to retrieve your current poketeam...\nTYPE '2' to add your own custom Pokemon\nTYPE '0' to CLOSE PROGRAM"))

server_query.getPokeList(userReq)