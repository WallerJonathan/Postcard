import requests
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Gets the info from the page
# PRECONDITION: Nothing
# POSTCONDITION: Returns the info in a dictionary
def getInfo():
    try:
        response = requests.get(url = "https://postcard-navy.vercel.app/api/survey")

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

    print(response)
    print(response.status_code)

    response.encoding = 'utf-8' # Optional: requests infers this internally
    returnedInfo = response.json()
    
    return returnedInfo

# Sends the info to the page
# PRECONDITION: data (the data from a json file)
# POSTCONDITION: None
def sendInfo(data):
    response = requests.post(url = "https://postcard-navy.vercel.app/api/survey", json={'key':data})
    returnedInfo = response.json()
    print(returnedInfo)



app = Flask("https://jwaller.pythonanywhere.com/")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])
@cross_origin()
def api():
    recieved = request.get_json()
    #newData = 
    return "hello"

api()

#print(getInfo())
#sendInfo("nuuu")
