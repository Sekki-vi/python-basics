# Functions
# A part of your code thats used to cause an effect or evaluate a value.
# Can come from: python built-in functions, modules, or your own functions.

# fucntions take in arguments
# the string in this print fucntion is an argument
print("Hello future Python programmer!")

# Function Execution
# 1. Check function name
# 2. Checks arguments passed
# 3. Jumps into the function code
# 4. Executes the function code
# 5. Returns to your code
# 6. Resumes execution

# Function Arguments
# Arguments are the values passed to a function when it is called.
# Arguments can be:
# - Positional arguments
# - Keyword arguments
# - Default arguments
# - Variable length arguments
# - Keyword variable length arguments

print("Hello", "future", "Python", "programmer!")
print("Hello futre\n Python programmer!")

# Keyword argument example
# end is a keyword argument with "\n" as the default value
print("Hello", end=" ")
print("future", end=" ")
print("Python", end=" ")
print("programmer!", end=" ")
print("\n")

# Keyword argument example
print("Hello", "future", "Python", "programmer!", sep="")

# Default argument example
print("Hello", "future", "Python", "programmer!", sep=" ", end="\n")

# LOL
print("Hello", "future", "Python", "programmer!", sep="\U0001F40D")

# Concatenation example
# Spaces are only added in quotes
# without quotes, spaces are ignored
# you can use the + operator to concatenate strings
# please note that this is not a good practice
print("Hello" + " "        "future" + " " + "Python" + " " + "programmer!")

# Can also use single quotes for strings
print('My age is 25')

# Concatenations need to be matching the data type of the strings
print("My age is " + str(25))