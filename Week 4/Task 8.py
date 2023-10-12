temp = []
listlength = "a"

while not listlength.isdigit():
    listlength = input("Please select a list length")

for x in range(1, (int(listlength) + 1)):
    tempadd = int(input("Please enter a Temp value"))
    temp.append(tempadd)

avgtemp = sum(temp) / 6

print("The highest temp was " + str(max(temp)) + " The lowest was " + str(min(temp)) + " and the average was ",
      avgtemp)
