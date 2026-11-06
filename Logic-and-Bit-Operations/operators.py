# logical operators
age1 = 24
age2 = 16

# logical operators are used to combine multiple conditions
# and operator returns true if both conditions are true
# or operator returns true if at least one condition is true
if age1 >= 18 and age2 >= 18:
    print("Both of you are adults")
elif age1 >= 18 or age2 >= 18:
    print("One of you is an adult")
else:
    print("Both of you are not adults")

# not operator returns true if the condition is false
# and returns false if the condition is true
is_hungry = False
if(not is_hungry):
    print("You are not hungry")