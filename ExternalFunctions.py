import json
import random


# pre-conditions: pass in the dictionary and file path of the json file
# post-conditions: creates a json file in the file path
def makeJson(myDict, filePath):
    try:
        with open(filePath, "w") as json_file:
            json.dump(myDict, json_file, indent=4)
        print(f"The JSON file '{filePath}' has been created.")
    except Exception as e:
        print(f"An error occurred: {e}")


# pre-conditions: takes in a list
# post-condtions: shuffles the list (but doesn't return the list)
def shuffleList(L):
    random.shuffle(L)

