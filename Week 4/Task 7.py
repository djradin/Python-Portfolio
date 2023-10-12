temp = [0, 0, 0, 0, 0, 0]
for x in range(1, 7):
    temp[x-1] = int(input("Please enter a Temp value"))

avgtemp = sum(temp) / 6

print("The highest temp was " + str(max(temp)) + " The lowest was " + str(min(temp)) + " and the average was ",
      avgtemp)
