import os
from flask import Flask, render_template, json, jsonify, current_app as app, request
from datetime import date
#for api requests 
import requests



app = Flask(__name__, static_folder="static")
json_info = ""
#the professtional way to create a server diirectory for an api
@app.route('/api/v1/akeena', methods=['GET'])
def akeena_json():
    
    #computer finds the pathway 
    akeena_info = os.path.join(app.static_folder,'data','album.json')
    #computer acually reads information, the r stands for reading 
    #meaning the computer is reading the information at the location 
    #specified in akeena_info, which is the album file thats my diy api
    #stores the infomation as a variable, json_data could be named anything
    with open(akeena_info,'r') as json_data:
        #the computer reads the above info as a string, not a json object 
        #it reads it as raw data, that's why we need to specify to the
        #computer that this 
        #           build in function, that takes whatever you give it and turns it
        # into json
        json_info = json.load(json_data)
        #this returns the above info to the browser
        #json_info = the present jsonify = the box + the wrapping
        return jsonify(json_info)

#this is the endpoint for the raw information for all the movies 
#inside the movies api json that we downloaded 

#this code finds the raw data for the movies.json file then 
#turns it into a json file for the computer to understand
@app.route('/api/v1/movies')
def every_movie():
    global json_info
    movies_path = os.path.join(app.static_folder, 'data','movies.json')
    with open(movies_path,'r') as raw_json:
        json_info = json.load(raw_json)
    return jsonify(json_info)

#this will be the endpint for the clean, templated verison of the
#information for the json file 
@app.route('/api/v1/movies/movie_title', methods=['GET'])
def movie_title():
    movies_path = os.path.join(app.static_folder, 'data','movies.json')
    with open(movies_path,'r') as raw_json:
        json_info = json.load(raw_json)
    results = []
    if 'title' in request.args:
        #stores the results of the title the user put into the url
        title = request.args['title']
        #goes through the movies.json file and searches for the movie (by object)    
        for movie in json_info:
            #if the titles match,  
            if title in movie['title']: 
                #appends information off the title 
                results.append(movie)
    if len(results) < 1:
        return "No requests found"
    return render_template("moviehub.html", results=result)



@app.route('/index')    
def index():
    name = "Akeena"
    group_names= ['Akeena', 'Fatou','Joseph N', 'Richlove']
    return render_template('index.html', greeting=name, groups= group_names)

@app.route('/richlove')
def richlove():
    return render_template('richlove.html')
@app.route('/nasa')
def show_nasa_img():
    #this information comes from the import datetime
    today = str(date.today())
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    data = response.json()
    return render_template('nasa.html',data=data)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')