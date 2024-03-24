import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_plant_data import get_plant_data  

app = Flask(__name__)

def plant_temp():
    timestamps, temp, hum, soil_moisture = get_plant_data(10)  
    # ... resten af din kode ...

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plant')
def plant():
    plant_temperature = plant_temp()
    plant_humidity = plant_hum()
    return render_template('plant.html' , plant_temperature = plant_temperature, plant_humidity = plant_humidity)

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

app.run(debug=True)

