import requests
import json
from fastapi import FastAPI, Request, UploadFile, Body, Cookie, File, Form, Header, Path, Query

app = FastAPI() # Probably won't use

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

def sendInfo(data):
    response = requests.post(url = "https://postcard-navy.vercel.app/api/survey", json={'key':data})
    returnedInfo = response.json()
    return returnedInfo

#print(getInfo())
#print(sendInfo("y"))