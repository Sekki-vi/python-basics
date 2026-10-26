# Example 1
# This will print "The condition is true" because True is always true
if True:
    print("The condition is true")

# Example 2
# This will ask the user for their age and print "You are an adult" if they are 18 or older, otherwise "You are a minor"
age = int(input("How old are you?"))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 3
# This will ask the user for a number and print "The number is positive" if the number is greater than 0, 
# "The number is negative" if the number is less than 0, otherwise "The number is zero"
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# any condition that is not empty is considered true, otherwise it is considered false
if (5,10): # this is a tuple
    print("hello") # this will print "hello" because 5 and 10 are in the tuple

if (): # this is an empty tuple
    print("hello") # this will not print anything because the tuple is empty

# 0 is considered false
if (0): # this is 0
    print("hello") # this will not print anything because 0 is considered false

# 1 is considered true
if (1): # this is 1
    print("hello") # this will print "hello" because 1 is considered true