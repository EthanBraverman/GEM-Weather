# Introduction to the program, and asks the user to log in.
print("Welcome to GEM Weather!")
print("")
print("Please log in.")

# Database of users and their respective passwords and names.
users = ["ethan", "gianni", "minsky"]
names = ["Ethan", "Gianni", "Mrs. Minsky"]
passwords = ["123", "456", "789"]

access_granted = False

#Asks the user for their username and password and checks them against the database. Access is granted if the username and password match.
while access_granted == False:
    print("------------------")
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
    else:
        print("User not found. Please try again.")

print("")
print("continued")