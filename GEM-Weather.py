#imports
import requests

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Database of users and their respective passwords and names.
users = ["user1", "user2", "user3"]
names = ["name1", "name2", "name3"]
passwords = ["pass1", "pass2", "pass3"]

#API Keys needed for the program to function.
positionstack_apikey = "api key"
tomorrow_apikey = "api key"

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

    def title_case(string):
        return " ".join(word.capitalize() for word in string.split())

    if len(state) == 2:
        street_address_formatted = title_case(address) + ", " + title_case(city) + ", " + state.upper() + " " + zip_code
    else:
        street_address_formatted = title_case(address) + ", " + title_case(city) + ", " + title_case(state) + " " + zip_code

    print("The location you entered is: " + street_address_formatted)
    location_correct_readable = input("Is this correct? [y/n] ")
    print("")
    if location_correct_readable == "y":
        location_correct = True
    else:
        print("Please re-enter your location.")
        print("------------------------------")

geocode_data = requests.get("https://api.positionstack.com/v1/forward?access_key=" + positionstack_apikey + "&query=" + street_address_formatted).json()

def lat(geocode_data):
    latitude = geocode_data["data"][0]["latitude"]
    return latitude

def lon(geocode_data):
    longitude = geocode_data["data"][0]["longitude"]
    return longitude

location = str(lat(geocode_data)) + ", " + str(lon(geocode_data))

forecast_data = requests.get("https://api.tomorrow.io/v4/weather/realtime?location=" + location + "&apikey=" + tomorrow_apikey).json()

wants_to_continue = True

while wants_to_continue == True:
    print("Please select an option by entering its corresponding number.")
    print("------------------------------------")
    print("1. Temperature")
    print("2. Chance of rain")
    print("3. Humidity")
    print("4. Wind speed")
    print("")
    option = input("Option: ")
    print("")

    if option == "1" or option == "temperature" or option == "Temperature" or option == "1. Temperature":
        temperature_c = forecast_data["data"]["values"]["temperature"]
        temperature_f = round((temperature_c * 9 / 5) + 32)
        print("The temperature at " + street_address_formatted + " is " + str(temperature_f) + "°F.")
        option_valid = True
    elif option == "2" or option == "chance of rain" or option == "Chance of rain" or option == "2. Chance of rain":
        chance_of_rain = forecast_data["data"]["values"]["precipitationProbability"]
        print("The chance of rain at " + street_address_formatted + " is " + str(chance_of_rain) + "%.")
        option_valid = True
    elif option == "3" or option == "humidity" or option == "Humidity" or option == "3. Humidity":
        humidity = forecast_data["data"]["values"]["humidity"]
        print("The humidity at " + street_address_formatted + " is " + str(humidity) + "%.")
        option_valid = True
    elif option == "4" or option == "wind speed" or option == "Wind speed" or option == "4. Wind speed":
        wind_speed_m_s = forecast_data["data"]["values"]["windSpeed"]
        wind_speed_mph = round(wind_speed_m_s * 2.23694)
        print("The wind speed at " + street_address_formatted + " is " + str(wind_speed_mph) + " mph.")
        option_valid = True
    else:
        print("That is not a valid option.")
        option_valid = False

    print("")

    if option_valid == False:
        wants_to_continue = True
    elif option_valid == True:
        wants_to_continue_readable = input("Would you like to select another option? [y/n] ")
        print("")
        if wants_to_continue_readable == "y":
            wants_to_continue = True
        else:
            wants_to_continue = False

print("Thank you for using GEM Weather. Have a great day!")
