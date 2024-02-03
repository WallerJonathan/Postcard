# import the modules
import requests
import json

# Open the data file from the user's answers
file = open('example.json')
data = json.load(file)

# Define a business ID
business_id = ''

# Define the API Key, Endpoint, and Header
API_KEY = "gkJViDC5De-32z-KWCt06tDdcOSyD1ip_A0LoCc712p-UN2pB9LBj4f7ctcnaXirEnDDLhJrSguuLoKPmizKtbF1P3lG9ArDBP0kQ9TZYm7yXn0zoFxs4hBy0HW9ZXYx"
ENDPOINT_SEARCH = 'https://api.yelp.com/v3/businesses/search'
ENDPOINT_DETAILS = 'https://api.yelp.com/v3/businesses/{}'.format(business_id) # must run this to replace any business_id
ENDPOINT_REVIEWS = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id) # must run this to replace any business_id
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define the parameters + extra stuff from json file
days = 3 # Total number of days, calculated from the json file PLACEHOLDER VALUE PLACEHOLDER VALUE PLACEHOLDER VALUE
selectedInterests = data["responses"][2]["answer"] # All of the selected interests (for destinations) from json file
placesPerInterest = (3*days)//len(selectedInterests) # 3 places per day, placesPerInterest is self explanitory
extraPlaces = (3*days) % len(selectedInterests) # Extra number of places we must return
selectedLocation = "Cancun" # Destination they want to travel to PLACEHOLDER VALUE PLACEHOLDER VALUE PLACEHOLDER VALUE
# PARAMETERS WILL CHANGE THROUGHOUT FILE
PARAMETERS = {'term': selectedInterests[0],
              'limit': 25,
              'offset': 0,
              'radius': 10000,
              'location': selectedLocation}

# For testing
print(placesPerInterest)
print(extraPlaces)

# Testing stuff (useful?)
lengths = [] # Stores number of selections per answer
for i in data["responses"]:
    print(i)
    ans = i['answer']
    lengths.append(len(ans))

    print("\t", ans)
    for j in ans: # For each set of answers per question
        print("\t\t", j)
    print("")
print(lengths)

# Create a list with 3*days destinations (stored as "BUS_NAME;;RATING;;BUS_ID")
# Uses peron intrests and gives back events and/or destinations (Question 3, Index 2 of data["responses"])
finDestinations = []
for i in range(3):
    myOffset = (i*placesPerInterest) + 1
    for interest in selectedInterests: # in len(selectedInterests) or 1 to conserve
        PARAMETERS = {'term': interest,
                    'limit': 25,
                    'offset': myOffset,
                    'radius': 10000,
                    'location': selectedLocation}

        # Make request to Yelp API
        response = requests.get(url = ENDPOINT_SEARCH, params = PARAMETERS, headers = HEADERS)

        # Convert JSON string to a list
        business_data = response.json()

        # Add placesPerInterest many places to finDestination
        bus = 0
        while(bus < placesPerInterest):
            finDestinations.append((str)(business_data['businesses'][bus]['name']) + ",," +
                                (str)(business_data['businesses'][bus]['rating']) + ",," +
                                (str)(business_data['businesses'][bus]['id']))
            bus += 1
        # Adds an extra place from the interest if needed
        if extraPlaces > 0:
            finDestinations.append((str)(business_data['businesses'][bus]['name']) + ",," +
                                (str)(business_data['businesses'][bus]['rating']) + ",," +
                                (str)(business_data['businesses'][bus]['id']))
            extraPlaces += -1

print(finDestinations)