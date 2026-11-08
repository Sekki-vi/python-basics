# Hierarchy of exceptions is the order in which exceptions are caught.

try:
    x = int(input('Enter a number: '))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ArithmeticError:
    print('Calculation failed.')
except:
    print('Something else went wrong')

print('All done!')

try:
    x = int(input('Enter a number: '))
    y = 1 / x
    print(y)
except (ZeroDivisionError, ArithmeticError):
    print('You cannot divide by zero')
except ArithmeticError:
    print('Calculation failed.')
except:
    print('Something else went wrong')

print('All done!')

# Errors can be handled inside the function
def calculate_user_input():
    try:
        x = int(input('Enter a number: '))
        y = 1 / x
        print(y)
    except:
        print('Something else went wrong')
        raise

calculate_user_input()

# Or outside the function
def calculate_user_input():
    x = int(input('Enter a number: '))
    y = 1 / x
    print(y)

try:
    calculate_user_input()
except (ZeroDivisionError, ArithmeticError):
    print('You cannot divide by zero')
except ArithmeticError:
    print('Calculation failed.')
except:
    print('Something else went wrong')

print('All done!')