# Introduction to the program, and asks the user to log in.
print("Welcome to GEM Weather!")
print("")
print("Please log in.")

# Database of users and their respective passwords and names.
users = ["user1", "user2", "user3"]
names = ["name1", "name2", "name3"]
passwords = ["pass1", "pass2", "pass3"]

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
