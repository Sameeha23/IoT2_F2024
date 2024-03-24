import sqlite3
from datetime import datetime
from time import sleep

def get_plant_data(number_of_rows):
    query = """SELECT * FROM plant ORDER BY datetime DESC LIMIT ?;""" 
    datetimes = []
    temperatures = []
    humidities = []
    soil_moistures = []  
    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query, (number_of_rows,))
        rows = cur.fetchall()
        for row in reversed(rows):
            datetimes.append(row[0])
            temperatures.append(row[1])
            humidities.append(row[2])
            soil_moistures.append(row[3])  
        return datetimes, temperatures, humidities, soil_moistures

    except sqlite3.Error as sql_e:
        print(f"sqlite error occurred: {sql_e}")
        conn.rollback()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if conn:
            conn.close()

get_plant_data(10)  

