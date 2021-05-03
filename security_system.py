known_users = ["Bob", "Alex", "Martina", "Claire", "Joanne", "Amit", "Soham"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().title()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No worries! I did not want you to leave anyway")


    else:
        print("Hmm! I don't think I have met you yet {}!".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        if add_me == "n":
            print("No worries, see you later")
