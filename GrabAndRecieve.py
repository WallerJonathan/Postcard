import requests
import json

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

#print(getInfo())
#sendInfo("nuuu")
