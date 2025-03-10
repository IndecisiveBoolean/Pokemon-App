import psycopg2
import poke_db.connect_info as connect_info
import poke_db.server_update as server_update

conn = None
curs = None

def getPokeList (userResp):
    if userResp == 1 :
        try:
            conn = psycopg2.connect(
                host = connect_info.hostname,
                dbname = connect_info.database,
                user = connect_info.username,
                password = connect_info.pwd,
                port = connect_info.port_id
            )

            # print(conn)
            curs = conn.cursor()

            curs.execute('SELECT * FROM pokemonBuild')
            totalPokes = curs.fetchall()
            
            
            currentNum = 1
            
            for x in totalPokes:

                print(f"{currentNum}: {x}")
                currentNum += 1
                            
        except Exception as error:
            print(error)
        finally:
            if curs is not None:
                curs.close()
            if conn is not None:
                conn.close()
    elif userResp == 0:
        return("Alright, closing program...goodbye Space Cowboy")
    elif userResp == 2:
        # MOVE THIS TO IT'S OWN FILE
        print("Let's add a new Pokemon, first I'll need the following information from you")
        
        getName = input("What is your Pokemon's name?")
        getType = input("What is your Pokemon's type?")
        getAtt = int(input("What is your Pokemon's attack?"))
        getDef = int(input("What is your Pokemon's defense?"))
        getHealth = int(input("What is your Pokemon's health?"))
        getEnergy = int(input("What is your Pokemon's energy?"))
        getLevel = int(input("What is your Pokemon's level?"))
        
        server_update.updatePokeList(getName, getType, getAtt, getDef, getHealth,getEnergy,getLevel)
        
        return("Pokemon Added!")
    else:
        return("something went wrong")
