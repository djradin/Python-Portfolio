numset = False

while not numset:
    num = int(input("Please enter a number between 0 and 12"))
    if num in range(0,13):
        num12 = num * 12
        print(str(num) + " x 12 = " + str(num12))
    else:
        print("Invalid number entered.")