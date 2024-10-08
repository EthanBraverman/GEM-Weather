# API Keys
positionstack_apikey = "eb3a8269f916521b7c4875580c2bae19"
tomorrow_apikey = "ri3S35dnqBoohgKAVQVS8Npu9xoVSgk0"

location_is_correct = False

while location_is_correct == False:
    print("Please enter your location")
    print("--------------------------")
    location_address = input("Address: ")
    location_city = input("City: ")
    location_state = input("State: ")
    location_zip_code = input("Zip Code: ")

    location = [location_address, location_city, location_state, location_zip_code]
    location_readable = location[0] + ", " + location[1] + ", " + location[2] + " " + location[3]

    print("")
    print("Your current location is: ")
    print(location_readable)
    print("")
    location_is_correct = input("Is this correct? [y/n]: ")

    if location_is_correct == "y":
        location_is_correct = True
        print("")
    else:
        location_is_correct = False
        print("")

geocode = "https://api.positionstack.com/v1/forward?access_key=" + positionstack_apikey + "&query=" + location_readable

coordinates = ["40.117128", "-74.854373"]
latlon = coordinates[0] + "," + coordinates[1]

forecast = "https://api.tomorrow.io/v4/weather/forecast?location=" + latlon + "&apikey=" + tomorrow_apikey

weather_options = ["1. Conditions", "2. Temperature", "3. Chance of Rain", "4. High and Low", "5. Hourly Forecast"]

print("Weather Options")
print("---------------")
print(weather_options[0])
print(weather_options[1])
print(weather_options[2])
print(weather_options[3])
print(weather_options[4])
print("")
print("Please select an option by typing in the corresponding number:")
selected_option = int(input(""))
'''
if selected_option == 1:
    #
elif selected_option == 2:
    #
elif selected_option == 3:
    #
elif selected_option == 4:
    #
elif selected_option == 5:
    #
'''