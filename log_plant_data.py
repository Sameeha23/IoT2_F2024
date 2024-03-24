import sqlite3
from datetime import datetime
from time import sleep

def create_table():
    query = """CREATE TABLE IF NOT EXISTS plant (datetime TEXT NOT NULL, temperature REAL NOT NULL, humidity REAL NOT NULL, soil_moisture REAL NOT NULL);"""
    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as sql_e:
        print(f"sqlite error occurred: {sql_e}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.close()

def log_plant_data():
    while True:
        query = """INSERT INTO plant (datetime, temperature, humidity, soil_moisture) VALUES(?, ?, ?, ?)""" 
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")  # Use %Y for full year
        
        data = (now, get_temperature(), get_humidity(), get_soil_moisture())

        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query, data)
            conn.commit()
        except sqlite3.Error as sql_e:
            print(f"sqlite error occurred: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            if conn:
                conn.close()
        sleep(1)

create_table()
log_plant_data()
