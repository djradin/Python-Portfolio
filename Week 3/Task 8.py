num = int(input("Please enter a number."))

if num < 0:
    numtim = 12
    while numtim > -1:
        print(numtim * 12)
        numtim = numtim - 1
else:
    numtim = 0
    while numtim < 13:
        print(numtim * 12)
        numtim = numtim + 1