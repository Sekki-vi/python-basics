# scopes
num = 100

def input_number():
    global own_num
    own_num = 50
    result = int(input("Enter a number: ")) * own_num
    return result

input_number()

print(own_num)

# global variable is accessible inside the function
# local variable is accessible only inside the function

x = 30
def my_function():
    global x
    x = 20

my_function()
print(x)