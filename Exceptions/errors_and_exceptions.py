# Errors are issues in the code that prevent the program from running.
try:
    name = "Lydia"
    print('My name is ' + naem)
except:
    print('Something went wrong')

print('All done')

try:
    x = int(input("Enter a number:"))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Please enter an integer")
except:
    print("something else went wrong")

print('All done')