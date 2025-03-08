# This is an app that generates a basic pokemon team for you and allows you to delete and add new pokemon at will.

# Prompt user about program DONE
# Access database of pokemn DONE
# display available pokemon to user DONE
# prompt use to add pokemon (select from list?)

import poke_db.server_query as server_query

print("WELCOME TO POKEGEN")

userReq = int(input("TYPE '1' if you'd like to retrieve your current poketeam...\nTYPE '2' to add your own custom Pokemon\nTYPE '0' to CLOSE PROGRAM"))

print(server_query.getPokeList(userReq))

# server_query.curs.execute("select * from pokemonBuild")
# print(server_query.curs.fetchall())



# create table pokemonBuild (
#     name VARCHAR(255),
#     role VARCHAR(255),
#     attack INT,
#     defense INT,
#     health INT,
#     energy INT,
#     level INT
#     );

# INSERT INTO pokemonBuild (name, role, attack, defense, health, energy, level)
# VALUES ('Piplup', 'water', 22, 19, 243, 499, 24);

