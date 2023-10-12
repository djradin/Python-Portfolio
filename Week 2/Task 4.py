students = int(input("How many students?"))
sweets = int(input("How many sweets?"))
sweetsper = sweets // students
sweetsrem = sweets % students
print("The " + str(students) + " students will get " + str(sweetsper) + " sweets each," +
      " with a remainder of " + str(sweetsrem) + " sweets remaining.")