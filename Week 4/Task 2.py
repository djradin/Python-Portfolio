def lettercheck():
    lower = 0
    upper = 0
    word = input("Enter a word to check upper and lower case letters")
    for i in word:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1

    print("There are " + str(lower) + " lower case letters and " + str(upper) + " upper case letters in the word " +
          word + ".")

lettercheck()
