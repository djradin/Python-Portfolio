student = int(input("How many students?"))
group = int(input("How big are the groups?"))
groupamm = student // group
groupleft = student % group
print("There will be " + str(groupamm) + " groups of " + str(group) +
      " students, with a smaller group of " + str(groupleft) + " people.")
