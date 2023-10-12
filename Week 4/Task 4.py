word = input("Please enter a word ")
wordlen = len(word)
if wordlen > 1:
    word = word[:-1]
    print(word)
else:
    print(word)