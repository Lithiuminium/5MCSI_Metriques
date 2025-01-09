from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__) 

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/histogramme/')
def histogramme():
    try:
        response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
        raw_content = response.read()
        json_content = json.loads(raw_content.decode('utf-8'))
        results = []
        for list_element in json_content.get('list', []):
            dt_value = list_element.get('dt')  # Utilisez dt_txt pour la date/heure
            temp_kelvin = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin à Celsius
            results.append({'Jour': dt_value, 'temp': temp_kelvin})  # Correction de la variable ici
        return jsonify(results=results)  # Correctement indenté à ce niveau

    except Exception as e:
        return jsonify({'error': f"Une erreur est survenue : {str(e)}"})

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin à °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Commentaire inutile ici
  
if __name__ == "__main__":
    app.run(debug=True)
