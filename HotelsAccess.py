# import the required  modules
import requests
import json
from ExternalFunctions import *
from GrabAndRecieve import *
from datfile import *

# clears the dictionaries
reigonResponse = {}
hotelResponse = {}

# sample input location to simulate user response
inputLocation = "Cancun"

# checks if place is already on file
reigonID = checkForPlace(inputLocation)

# if place is not on file, make an API request to get the reigon id and save it on file
if reigonID == None:
    # parameters for API request
    reigonSearchURL = "https://hotels-com-provider.p.rapidapi.com/v2/regions"
    reigonSearchParams = {"query":inputLocation,"domain":"US","locale":"en_US"}
    headers = {
        "X-RapidAPI-Key": "9170734aecmsh7a7f0409f2cdbffp1b96c6jsn3190dafdbc72",
        "X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com"
    }

    # make request to hotels.com API for reigon info
    reigonResponse = (requests.get(url=reigonSearchURL, params=reigonSearchParams, 
                                   headers=headers)).json()
    # obtains reigon ID
    reigonID = reigonResponse["data"][0]["gaiaId"]

    # save place on file
    writeNewPlace(inputLocation, reigonID)
# else if place already exists, 
# use the reigon id obtained to make the api request for hotels


# parameters for API request for hotel info
hotelSearchURL = "https://hotels-com-provider.p.rapidapi.com/v2/hotels/search"
checkInDate = "2024-09-25"
checkOutDate = "2024-09-28"
hotelBudgetPerNight = "200"
hotelSearchParams = {"region_id":reigonID,"locale":"en_US","checkin_date":checkInDate,
            "sort_order":"RECOMMENDED","adults_number":"2","domain":"US",
            "checkout_date":checkOutDate,"lodging_type":"HOTEL,APARTMENT,BED_AND_BREAKFAST",
            "price_min":"20","star_rating_ids":"3,4,5","meal_plan":"FREE_BREAKFAST",
            "page_number":"1", "price_max":hotelBudgetPerNight,"amenities":"WIFI,PARKING",
            "payment_type":"PAY_LATER,FREE_CANCELLATION", "guest_rating_min":"8",
            "available_filter":"SHOW_AVAILABLE_ONLY"}

# make request to hotels.com API
hotelResponse = requests.get(url=hotelSearchURL, params=hotelSearchParams, 
                             headers=headers).json()

# debugger
# # Specify the filename where you want to save the JSON data
# filename = 'C:/soham/tartan hacks/hotelResponse.json'
# # Open the file in write mode ('w') and dump the JSON data
# with open(filename, 'w') as file:
#     json.dump(hotelResponse, file, indent=4)
# print(f"JSON data has been written to {filename}")

# Each hotel variable contains the hotel name(str), customer rating out of 5(float),
# price per day(str) and total price incl. of taxes(str), and url of the pic(str) 
hotel1 = [hotelResponse["properties"][0]["name"], 
          hotelResponse["properties"][0]["reviews"]["score"]/2, 
          hotelResponse["properties"][0]["price"]["options"][0]["formattedDisplayPrice"], 
          hotelResponse["properties"][0]["price"]["displayMessages"][1]["lineItems"][0]["value"],
          hotelResponse["properties"][0]["propertyImage"]["image"]["url"]]
hotel2 = [hotelResponse["properties"][1]["name"], 
          hotelResponse["properties"][1]["reviews"]["score"]/2, 
          hotelResponse["properties"][1]["price"]["options"][0]["formattedDisplayPrice"], 
          hotelResponse["properties"][1]["price"]["displayMessages"][1]["lineItems"][0]["value"],
          hotelResponse["properties"][1]["propertyImage"]["image"]["url"]]
hotel3 = [hotelResponse["properties"][2]["name"], 
          hotelResponse["properties"][2]["reviews"]["score"]/2, 
          hotelResponse["properties"][2]["price"]["options"][0]["formattedDisplayPrice"], 
          hotelResponse["properties"][2]["price"]["displayMessages"][1]["lineItems"][0]["value"],
          hotelResponse["properties"][2]["propertyImage"]["image"]["url"]]
hotelsList = [hotel1, hotel2, hotel3]
# print(hotelsList) # debugger