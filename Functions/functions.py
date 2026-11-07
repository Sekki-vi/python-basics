# functions
def input_number():
    return int(input("Enter a number: "))

# input1 = input_number()
# input2 = input_number()


def print_info(name, age=18):
    print(name, age)

print_info("John", 20)

def multi_func():
    result = int(input()) * 5
    return result

print(multi_func())