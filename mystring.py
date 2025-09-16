myString = "This is a string."
print(myString)
print(myString + " is of the data type " + str(type(myString)))

#Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#Working with input strings: The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:
name = input("What is your name? ")
print(name)

#Formatting output strings: When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))


