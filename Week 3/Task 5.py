pass1 = 0
pass2 = 1
passlen = 0
badpass = ["password", "letmein", "sesame", "hello", "justinbeiber"]
passset = 0
while passset == 0:
    pass1 = input("Please enter a password.")
    pass2 = input("Please enter your password again.")
    passlen = len(pass1)
    if passlen > 0 and pass1 == pass2 and pass1 not in badpass:
        print("Password set.")
        passset = 1
    else:
        if passlen == 0:
            print("No password entered.")
        elif pass1 in badpass:
            print("Weak password selected.")
        else:
            print("Passwords do not match.")
