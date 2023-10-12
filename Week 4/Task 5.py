convert = ""
while convert != "F" or convert != "C":
    temp = ""
    temp2 = ""
    convert = input("Enter which unit to convert from F or C")
    if convert == "C":
        while not temp.isdigit():
            temp = input("Please enter a celsius value ")

        temp2 = (int(temp) * 1.8) + 32
        print(str(temp) + " Celsius in Fahrenheit is " + str(temp2) + " Fahrenheit")
    elif convert == "F":
        while not temp.isdigit():
            temp = input("Please enter a celsius value ")

        temp2 = (int(temp) - 32) / (5/9)
        print(str(temp) + " Fahrenheit in Celsius is " + str(temp2) + " Celsius")
