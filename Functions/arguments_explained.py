# arguments explained
age = 22
def multiply(num):
    num *= 2
    print("in multiply: ", str(num))

multiply(age)
print("outside multiply: ", str(age))

# the value of age is not changed because it is a local variable

# with lists, the value is changed because it is a mutable object
numbers = [1, 2, 3, 4, 5]
def multiply(numbers):
    numbers *= 2
    print("in multiply: ", str(numbers))

multiply(numbers)
print("outside multiply: ", str(numbers))

def my_function(*argv):
    print(argv)


my_function('Hello', 'World!')