
from Application import app
from flask import render_template


@app.route("/", methods = ["POST","GET"])
def home():
    return render_template('Home_D.html')

@app.route("/destination_moon",methods = ["POST","GET"])
def destination_Moon():
    return render_template('destination_moon.html')

@app.route("/destination_mars", methods = ["POST","GET"])
def destination_Mars():
    return render_template('destination_mars.html')

@app.route("/destination_europa", methods = ["POST","GET"])
def destination_Europa():
    return render_template('destination_europa.html')

@app.route("/destination_titan", methods = ["POST","GET"])
def destination_Titan():
    return render_template('destination_titan.html')

@app.route("/crew", methods = ["POST","GET"])
def crew():
    return render_template('crew.html')

@app.route("/technology", methods = ["POST","GET"])
def technology():
    return render_template('technology.html')

@app.route("/technology2", methods = ["POST","GET"])
def technology2():
    return render_template('technology2.html')

@app.route("/technology3", methods = ["POST","GET"])
def technology3():
    return render_template('technology3.html')