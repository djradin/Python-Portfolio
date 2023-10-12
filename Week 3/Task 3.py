pass1 = 0
pass2 = 1
passlen = 0

while passlen == 0 and pass1 != pass2:
    pass1 = input("Please enter a password.")
    pass2 = input("Please enter your password again.")
    passlen = len(pass1)
    if passlen > 0 and pass1 == pass2:
        print("Password set.")
    else:
        if passlen == 0:
            print("No password entered.")
        else:
            print("Passwords do not match.")
