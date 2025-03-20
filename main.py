# This is an app that generates a basic pokemon team for you and allows you to delete and add new pokemon at will.

# Prompt user about program DONE
# Access database of pokemn DONE
# display available pokemon to user DONE
# Update initial display to show pokemon as a list DONE
# prompt use to add pokemon (select from list?) DONE

# Adjust program to not close automatically but instead loop back to the main menu for options IN PROGRESS

import poke_db.server_query as server_query
import poke_db.server_update as server_update
import poke_db.server_delete as server_delete



print("WELCOME TO POKEGEN\n Do you want to access the program?")
progControl = input("Type 'Yes' to get started or 'No' to shutdown\n")

while progControl != 'No':
    
    userReq = int(input("TYPE '1' if you'd like to retrieve your current poketeam...\nTYPE '2' to add your own custom Pokemon\nTYPE '3' if you'd like to REMOVE a Pokemans\nTYPE '0' to CLOSE PROGRAM\n"))
    
    if userReq == 1: # 1 is list recover
        server_query.getPokeList(userReq)

    elif userReq == 2: # 2 is update
        print("Let's add a new Pokemon, first I'll need some information from you ")
        
        getName = input("What is your Pokemon's name?\n")
        getType = input("What is your Pokemon's type?\n")
        getAtt = int(input("What is your Pokemon's attack?\n"))
        getDef = int(input("What is your Pokemon's defense?\n"))
        getHealth = int(input("What is your Pokemon's health?\n"))
        getEnergy = int(input("What is your Pokemon's energy?\n"))
        getLevel = int(input("What is your Pokemon's level?\n"))
        
        server_update.updatePokeList(getName, getType, getAtt, getDef, getHealth,getEnergy,getLevel)

    elif userReq == 3:
        server_delete.removeFromPokeList()

    elif userReq == 0:
        print("Alright, closing program...See You Later Space Cowboy")
        break
else:
    print("Exiting Program\n")
    exit
    


