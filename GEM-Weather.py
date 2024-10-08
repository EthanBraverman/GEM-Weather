#imports
import requests

# Database of users and their respective passwords and names.
users = ["user1", "user2", "user3"]
names = ["name1", "name2", "name3"]
passwords = ["pass1", "pass2", "pass3"]

#API Keys needed for the program to function.
positionstack_apikey = "[api key]"
tomorrow_apikey = "[api key]"

# ----------------------------------------------------------------------

# Introduction to the program, and asks the user to log in.

access_granted = False

print("Welcome to GEM Weather!")
print("")
print("Please log in.")
print("--------------")

#Asks the user for their username and password and checks them against the database. Access is granted if the username and password match.
while access_granted == False:
    username = input("Username: ")
    password = input("Password: ")
    print("")
    if username in users:
        if password == passwords[users.index(username)]:
            name = names[users.index(username)]
            print("Login successful. Welcome to GEM Weather, " + name + "!")
            access_granted = True
        else:
            print("Incorrect password. Please try again.")
            print("-------------------------------------")
    else:
        print("User not found. Please try again.")
        print("---------------------------------")

print("")

location_correct = False

print("Please enter your location.")
print("---------------------------")

while location_correct == False:
    address = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")
    print("")

    street_address = address + ", " + city + ", " + state + " " + zip_code

    print("The location you entered is: " + street_address)
    location_correct_readable = input("Is this correct? [y/n] ")
    print("")
    if location_correct_readable == "y":
        location_correct = True
    else:
        print("Please re-enter your location.")
        print("------------------------------")

geocode_data = requests.get("https://api.positionstack.com/v1/forward?access_key=" + positionstack_apikey + "&query=" + street_address).json()

def lat(geocode_data):
    latitude = geocode_data["data"][0]["latitude"]
    return latitude

def lon(geocode_data):
    longitude = geocode_data["data"][0]["longitude"]
    return longitude

location = str(lat(geocode_data)) + ", " + str(lon(geocode_data))

forecast = requests.get("https://api.tomorrow.io/v4/weather/realtime?location=" + location + "&apikey=" + tomorrow_apikey).json()

print(forecast)
