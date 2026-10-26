# input() is a function that takes input from the user
input("How are you feeling today? ")

favorite_color = input("What is your favorite color? ")
print("Your favorite color is " + favorite_color)

# the input function always returns a string and takes a string as an argument
age = input("How old are you? ")
print(type(age)) # <class 'str'>

# to convert the input to an integer, we can use the int() function
age = int(input("How old are you? "))
print(type(age)) # <class 'int'>

# to convert the input to a float, we can use the float() function
age = float(input("How old are you? "))
print(type(age)) # <class 'float'>

# input prompts user to input some data from the console
# It accepts an optional parameter that can be used in order to write a message before the user input
# Always returns a string
# A program that doesn't use any input function is called a *deaf program*