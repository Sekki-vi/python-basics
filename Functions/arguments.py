# arguments
def print_info(name, age):
    print(name, age)

print_info("John", 20)
print_info(age=20, name="John")

def print_info(name, age=18):
    print(name, age)

print_info("John")
print_info("John", 20)
# order doesn't matter for named parameters
print_info(age=20, name="John")