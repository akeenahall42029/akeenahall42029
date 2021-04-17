from flask import Flask, render_template, request, current_app as app 
from sense_hat import SenseHat
from time import sleep
import sqlite3

sense = SenseHat ()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sucess',methods=['GET','POST'])
def sucess():
    message = request.form['message'] 
    user_name = request.form['user_name']
    #showing the message on the SenseHat 
    sense.show_message(message)
    #connect to database and insert message and name; connection pulls the data up
    conn = sqlite3.connect("./static/data/senseDisplay.db")
    #setting up curser ; curser points to your data and it can translate your query's output 
    curs = conn.cursor()
    curs.execute("INSERT INTO messages (name, message) VALUES((?),(?))",(user_name,message))
    conn.commit()
    #close database connection 
    conn.close()
    return render_template("sucess.html",message = message, user_name = user_name)
@app.route('/all', methods=['GET','POST'])
def all():
    #connect to database 
    conn = sqlite3.connect("./static/data/senseDisplay.db")
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message': row[1]}
        messages.append(message)
    conn.close()
    return render_template("all.html", messages = messages)

    
if __name__ == '__main__':
    app.run(debug = True, host ='0.0.0.0')