from flask import Flask, render_template, current_app as current_app

app = Flask(__name__)


@app.route('/')   
def index():
    return "Welcome to Akeena's Rainbow Project"
@app.route('/rainbow')
def rainbow():
    colorlinks = ['red','orange','yellow','green','blue','indigo','violet']
    
    return render_template("rainbow_temp.html",colorlinks=colorlinks)
    
@app.route('/red', methods=['GET'])
def redPage():
    color = 'RED'
    return render_template("colors.html",color = color)

@app.route('/orange',methods=['GET'])
def orangePage():
    color = 'ORANGE'
    return render_template("colors.html",color=color)

@app.route('/yellow',methods=['GET'])
def yellowPage():
    color = 'YELLOW'
    return render_template("colors.html",color=color)

@app.route('/green',methods=['GET'])
def greenPage():
    color = 'GREEN'
    return render_template("colors.html", color=color)

@app.route('/blue',methods=['GET'])
def bluePage():
    color = 'BLUE'
    return render_template("colors.html", color=color)

@app.route('/indigo',methods=['GET'])
def indigoPage():
    color = 'INDIGO'
    return render_template("colors.html", color=color)

@app.route('/violet',methods=['GET'])
def violetPage():
    color = 'VIOLET'
    return render_template("colors.html", color = color)

#bottom of the code 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')