from flask import Flask, jsonify
import json

app = Flask(__name__)

file = open('/home/jwaller/mysite/SendItinerary.json')
data = json.load(file)
print(data)

@app.route('/')
def work():
    return jsonify(data)