def numcheck():
    num = int(input("Enter a number between 0 and 100"))
    if num in range(0, 101):
        print("True")
    else:
        print("False")


numcheck()
