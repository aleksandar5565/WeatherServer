from flask import Flask, render_template

app = Flask(__name__)

temperature = 0
humidity = 0

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/weather")
def second():
    return render_template("weather.html", temp = temperature, hum = humidity)

@app.route("/getData/<temp>/<hum>")
def getData(temp, hum):
    global temperature, humidity
    temperature = temp
    humidity = hum
    return "Saved"

app.run(debug = True)