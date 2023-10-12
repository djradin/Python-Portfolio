nameans = False

while not nameans:
    name = input("What is your name")
    if name.isalpha():
        name = name.capitalize()
        print("Hello, " + name)
        nameans = True
    else:
        print("Names dont have numbers in them.")