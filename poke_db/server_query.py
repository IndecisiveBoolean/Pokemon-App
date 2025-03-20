import psycopg2
import poke_db.connect_info as connect_info
import time

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
                
            print("These are your current pokemon.")
            time.sleep(0.5)
            print("I'm sending you back to the main menu now!")
            time.sleep(2)
                            
        except Exception as error:
            print(error)
        finally:
            if curs is not None:
                curs.close()
            if conn is not None:
                conn.close()
    else:
        return("something went wrong")
