# Importing quality of life libraries

import os
import time

Lessonnum = ["Lesson 1 - ", "Lesson 2 - ", "Lesson 3 - ", "Lesson 4 - ", "Lesson 5 - ", "Lesson 6 - ", "Lesson 7 - ",
             "Lesson 8 - "]
Lessonsub = ["Introduction to Programming", "Variables and Types", "Control Statements", "Defining Functions",
             "Scripts and Modules", "Lists and Tuples", "Sets and Dictionaries", "I/O and File Handling"]

os.system("cls")

finish = False
choice = 0
blank_check = 0

# Introduction / selecting the desired set of data
# This is all in a while loop to allow you to go back to the top and visit another section
# Without needing to restart
# The same applies to the program_off loop, but I don't want to have the lesson list
# Print every time there is a wrong selection

while not finish:
    program_off = False
    print("Hello, please select a lesson to view its corresponding portfolio work.\n")
    time.sleep(1)
    print("The options are\n")
    time.sleep(0.65)
    for i in range(1, 9):
        print(Lessonnum[i - 1] + "\u001b[34;1m" "\u001b[4;1m" + Lessonsub[i - 1] + "\u001b[0;1m")
        time.sleep(0.45)
    while not program_off:
        choice = input("\nPlease select a number > ")
        blank_check = len(choice)
        if not choice.isalpha() and blank_check > 0:
            if int(choice) in range(1, 9):
                print("\nYou have selected " + Lessonsub[int(choice) - 1] + "\n")
                time.sleep(0.4)
                for i in range(1, 3):
                    print("\rLoading", end="")
                    time.sleep(0.45)
                    print("\rLoading.", end="")
                    time.sleep(0.45)
                    print("\rLoading..", end="")
                    time.sleep(0.45)
                    print("\rLoading...", end="")
                    time.sleep(0.45)
            else:
                print("\nNumber not valid, please choose a number between 1 and 8")
        else:
            print("\nSelection invalid, please try again.")
            time.sleep(0.25)
            choice = 10

        if int(choice) == 1:
            program_off = True
            batting_average = 48426 / (1014 - 162)
            rbatting_average = round(batting_average, 4)
            name = "0"
            tempC = 38.4
            tempF = (tempC * 1.8) + 32
            print("\rHello\n")
            time.sleep(0.75)
            while name.isdigit():
                name = input("What is your name? > ")
                if name.isdigit():
                    print("\nNames don't have numbers in them! Try again.\n")
                    time.sleep(0.35)
            print("\nHello, " + "\u001b[33;1m" + name.capitalize() + "\u001b[0;1m" + "!")
            time.sleep(0.55)
            print("Did you know that over the summer, the temperature in Yorkshire reached " + str(tempC) + "°C?")
            time.sleep(0.75)
            print(str(tempC) + "°C is equivalent to " + str(tempF) + "°F.\n")
            time.sleep(1)
            print("On the topic of Yorkshire, did you know that Geoffrey Boycott played 609 matches over his career,")
            time.sleep(0.65)
            print("In which he batted 1014 times, was not out 162 times, and scored a total of 48426 runs?\n")
            time.sleep(0.65)
            print("This means he had a batting average of " "\u001b[32;1m" + str(rbatting_average) + "\u001b[0;1m"
                  " throughout his career.")
            time.sleep(0.75)
            print("Or, to be more precise " + "\u001b[32;1m" + str(batting_average) + "\u001b[0;1m\n")

