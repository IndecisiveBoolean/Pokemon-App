import psycopg2
import poke_db.connect_info as connect_info
import time

conn = None
curs = None

def removeFromPokeList ():
    try:
        conn = psycopg2.connect(
            host = connect_info.hostname,
            dbname = connect_info.database,
            user = connect_info.username,
            password = connect_info.pwd,
            port = connect_info.port_id
        )

        curs = conn.cursor()
        
        curs.execute('SELECT * FROM pokemonBuild') #change to variable instead of directly executing the SQL command
        totalPokes = curs.fetchall()
        
        print("These are your current pokemon.")
        time.sleep(0.5)
        
        for x in totalPokes:
            print(x)
            
        time.sleep(0.5)
        pokeToDelete = input("Please enter the NAME of your pokemon that you'd like to delete, or type 'cancel' to cancel deletion\n")
        
        # This can be cleaned up and streamlined
        
        if pokeToDelete == 'cancel':
            print("CANCELLING DELETION, Today is your lucky day Pokemans...")
            return()
        else:
            curs.execute(f"DELETE FROM pokemonBuild WHERE NAME = '{pokeToDelete}'")
            conn.commit()
            
            print(f"deleting {pokeToDelete}, please wait")
            time.sleep(1)
            print(f"{pokeToDelete} deleted, here is your updated Pokemans list.")
            
            curs.execute('SELECT * FROM pokemonBuild')
            totalPokes = curs.fetchall()
            
            print(totalPokes)
        
    except Exception as error:
        print(error)
    finally:
        if curs is not None:
            curs.close()
        if conn is not None:
            conn.close()
