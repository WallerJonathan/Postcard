import pickle

placesDict = {} 

# precondition: takes in a place (key)
# postcondition: 
    # opens the dat file and loads the dictionary
    # if a value in the dictionary == place_str, 
    # return the value, and return None otherwise.
def checkForPlace(place_str):
    # Open the places.dat file and load the placesDict
    with open('places.dat', 'rb') as file:
        placesDict = pickle.load(file)
        
    for key in placesDict:
        if placesDict[key] == place_str:
            return placesDict[key]
        else:
            return None

# precondition: takes in a place (key) and value
# postcondition: 
    # does not return anything
    # opens the dat file and loads the dictionary
    # assign the place (key) to the value in the dictiionary
    # opens the dat file and dump the dictionary in the file.
def writeNewPlace(place_str, value):
    # Open the places.dat file and load the placesDict
    with open('places.dat', 'rb') as file:
        placesDict = pickle.load(file)

    placesDict[place_str] = value

    with open('places.dat', 'wb') as file:
        pickle.dump(placesDict, file)
