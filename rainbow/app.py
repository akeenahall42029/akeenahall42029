from flask import Flask, render_template, current_app as current_app

app = Flask(__name__)


@app.route('/')   
def index():
    return "Welcome to Akeena's Rainbow Project"

@app.route('/red', methods=['GET'])
def redPage():
    return render_template("red.html")

@app.route('/orange',methods=['GET'])
def orangePage():
    return render_template("orange.html")

@app.route('/yellow',methods=['GET'])
def yellowPage():
    return render_template("yellow.html")

@app.route('/green',methods=['GET'])
def greenPage():
    return render_template("green.html")

@app.route('/blue',methods=['GET'])
def bluePage():
    return render_template("blue.html")

@app.route('/indigo',methods=['GET'])
def indigoPage():
    return render_template("indigo.html")

@app.route('/violet',methods=['GET'])
def violetPage():
    return render_template("violet.html")

#this goes at the bottom!
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')