import requests
import json
# import library for Flask, not all methods are used here
from flask import Flask, render_template, request, redirect, jsonify
# Init app
app = Flask(__name__)
""" 
Here are some sample API sources to test with. Please note, the dad-joke API is limited capacity (for free)
and requires registration 
"""
URL = "http://api.icndb.com/jokes/random?limitTo=[nerdy]"
URL2 = "https://dad-jokes.p.rapidapi.com/joke/type/knock-knock"
headers = {
    'x-rapidapi-key': "9fbf30bc6amsh6613788b5a52723p13d9a4jsna3b45112690b",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }


#App Routes
#The first route is the index route which is required. Best practice is to limit methods to those supported.
# Typical function show with a post method for form, otherise a default listing of all db entries
@app.route('/', methods=['POST', 'GET'])
def index():
    # r = requests.get(url = URL)
    # data = r.json()
    # joke = data['value']['joke']
    # return str(joke)

    r = requests.get(url = URL2, headers = headers)
    data = r.json()
    #print (data)
    joke = ('Q: ' + data['body'][0]['setup'] + '  A: ' + data['body'][0]['punchline'])
    return str(joke)

# API Routes
# API GET Query
@app.route('/api', methods=['GET'])
def api():
    r = requests.get(url = URL2, headers = headers)
    data = r.json()
    return data

    # r = requests.get(url = URL)
    # data = r.json()
    # return data

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)    
