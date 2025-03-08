import psycopg2
import poke_db.connect_info as connect_info
import time

conn = None
curs = None

def updatePokeList (name, role, attack, defend, health, energy, level):
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
        
        insert_script = 'INSERT INTO pokemonBuild (name, role, attack, defense, health, energy, level) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        insert_values = (name, role, attack, defend, health, energy, level)

        curs.execute(insert_script, insert_values)
        
        conn.commit()
        
        time.sleep(5)
        
        return(curs.fetchall())
        
    except Exception as error:
        print(error)
    finally:
        if curs is not None:
            curs.close()
        if conn is not None:
            conn.close()
