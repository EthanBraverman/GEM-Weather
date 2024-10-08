import asyncio as aio

async def main():
    # size fo the canvas
    set_size(400, 400)

    x = get_width()
    y = get_height()

    # making a random fucntion?
    import random
    random_num = random.randint(0, 300)

    # makes background a light blue color
    rect = Rectangle(x, y)
    rect.set_position(0, 0)
    rect.set_color('#b3d8ff')
    add(rect)

    def make_circle(x, y):
        # adds the white circles onto the screen
        circle = Circle(50)
        circle.set_position(x, y)
        circle.set_color(Color.white)
        add(circle)

    # makes circles
    make_circle(0, 100)
    make_circle(80, 0)
    make_circle(100, 170)
    make_circle(0, 250)
    make_circle(185, 280)
    make_circle(200, 20)
    make_circle(290, 170)
    make_circle(350, 280)
    make_circle(350, 0)
    make_circle(10, 400)
    make_circle(200, 400)

    # adds text to the screen over the circles
    txt = Text("Welcome To G.E.M Weather!")
    txt.set_position(24, 50)
    txt.set_color('#0070e6')
    txt.set_font("20pt Arial")
    add(txt)

    login_prompt_txt = Text("LOGIN BELOW")
    login_prompt_txt.set_position(x / 3, y / 4)
    login_prompt_txt.set_font("15pt Arial Narrow ")
    login_prompt_txt.set_color('#6f6bc2')
    add(login_prompt_txt)

    username = await async_input("Enter Username: ")
    password = await async_input("Enter Password: ")

    # print("Your in! ")

    # makes background a blue color
    rect2 = Rectangle(x, y)
    rect2.set_position(0, 0)
    rect2.set_color('#89afe0')
    add(rect2)

    # fucntion for Creating diagonal lines for the background
    def make_line(x1, y1, x2, y2):
        line = Line(x1, y1, x2, y2)
        line.set_color('#bdd4f2')
        add(line)

    # makes lines diagonally
    make_line(0, 0, x, y)
    make_line(100, 0, 400, 300)
    make_line(200, 0, 400, 200)
    make_line(300, 0, 400, 100)
    make_line(0, 100, 300, 400)
    make_line(0, 200, 200, 400)
    make_line(0, 300, 100, 400)

    ur_in_txt = Text("Welcome, " + username)
    ur_in_txt.set_position(x / 4.40, y / 5)
    ur_in_txt.set_font("20pt Arial Narrow ")
    ur_in_txt.set_color('#213b5c')
    add(ur_in_txt)

    # Gem weather in the top left corner of the screen
    gem_txt = Text("G.E.M Weather")
    gem_txt.set_position(0, 30, )
    gem_txt.set_font("15pt Arial Black")
    gem_txt.set_color('#0a2f61')
    add(gem_txt)

    plz_entr_txt = Text("Please enter your location Below in the following order")
    plz_entr_txt.set_position(10, 140)
    plz_entr_txt.set_font("12pt Arial Narrow")
    plz_entr_txt.set_color('#0a2f61')
    add(plz_entr_txt)

    locate_addy_txt = Text("Address: ")
    locate_addy_txt.set_position(30, 180)
    locate_addy_txt.set_font("12pt Arial Narrow")
    locate_addy_txt.set_color('#0a2f61')
    add(locate_addy_txt)

    locate_city_txt = Text("City: ")
    locate_city_txt.set_position(30, 200)
    locate_city_txt.set_font("12pt Arial Narrow")
    locate_city_txt.set_color('#0a2f61')
    add(locate_city_txt)

    locate_state_txt = Text("State: ")
    locate_state_txt.set_position(30, 220)
    locate_state_txt.set_font("12pt Arial Narrow")
    locate_state_txt.set_color('#0a2f61')
    add(locate_state_txt)

    locate_zip_code_txt = Text("ZipCode: ")
    locate_zip_code_txt.set_position(30, 240)
    locate_zip_code_txt.set_font("12pt Arial Narrow")
    locate_zip_code_txt.set_color('#0a2f61')
    add(locate_zip_code_txt)

    # asking the user for their address, city, state, and zipcode

    print("-------------------")
    address = await async_input("ADDRESS: ")
    city = await async_input("CITY: ")
    state = await async_input("STATE: ")
    zipcode = await async_input("ZIP CODE: ")
    print("-------------------")

    rect3 = Rectangle(x, y)
    rect3.set_position(0, 0)
    rect3.set_color('#cfd9fc')
    add(rect3)

    add(gem_txt)

    location_txt = Text("Your current location is: ")
    location_txt.set_position(x / 4.40, y / 5)
    location_txt.set_font("20pt Arial Narrow ")
    location_txt.set_color('#5c70b8')
    add(location_txt)

    current_location = (address + ", " + city + ", " + state + zipcode)

    current_location = Text(current_location)
    current_location.set_position(10, 150)
    current_location.set_font("15pt Arial Narrow ")
    current_location.set_color('#5c70b8')
    add(current_location)

    correct_txt = Text("Is Your current Location correct? Please answer below")
    correct_txt.set_position(10, 350)
    correct_txt.set_font("10pt Arial ")
    correct_txt.set_color('#5c70b8')
    add(correct_txt)

    correct = await async_input("Is your current location correct? [Y/N] ")

    wrong_maybe = Text("What's wrong " + username + "?")
    wrong_maybe.set_position(10, 100)
    wrong_maybe.set_font("20pt Arial Black")
    wrong_maybe.set_color('#0e0b63')

    while correct == "n" or correct == "N":

        add(rect2)
        add(plz_entr_txt)
        add(gem_txt)
        add(locate_addy_txt)
        add(locate_city_txt)
        add(locate_state_txt)
        add(locate_zip_code_txt)

        add(wrong_maybe)

        print("-------------------")
        address = await async_input("ADDRESS: ")
        city = await async_input("CITY: ")
        state = await async_input("STATE: ")
        zipcode = await async_input("ZIP CODE: ")
        print("-------------------")

        add(correct_txt)

        correct = await async_input("Is your current location correct? [Y/N] ")

        if correct == "y" or correct == "Y":
            add(rect3)

    make_line(0, 0, x, y)
    make_line(100, 0, 400, 300)
    make_line(200, 0, 400, 200)
    make_line(300, 0, 400, 100)
    make_line(0, 100, 300, 400)
    make_line(0, 200, 200, 400)
    make_line(0, 300, 100, 400)


aio.run(main())