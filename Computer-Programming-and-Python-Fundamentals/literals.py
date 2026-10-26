# Literals are the data values that are given directly to the program.
# Literal types:
# Integer literals
# - Octal numbers are prefixed with 0o
# - Hexadecimal numbers are prefixed with 0x
# - Binary numbers are prefixed with 0b

print(0o123)
print(0x123)
print(0b101)
print(1_234_567_890)

# Float literals
# - Float literals are numbers with a decimal point

print(123.456)

# Long floating point literals can also be written with 'e'
print(123.456e-2)

# String literals
# - String literals are sequences of characters enclosed in quotes
# - String literals can be single quotes or double quotes

print('Hello future Python programmer!')
print("Hello future Python programmer!")

# String literals can also be multi-line
print("Hello\n future\n Python\n programmer!")

# If you need to write a quote inside a string, you can use an escape character or the other type of quotes
print('He said, "Hello future Python programmer!"')
print("He said, 'Hello future Python programmer!'")

# Boolean literals
# - Boolean literals are True or False
# - Boolean literals can be used to represent truth values in the program
# - Boolean literals can be used to represent truth values in the program

print(True)
print(False)

# None is a special literal in Python that represents the absence of a value
print(None)

# Complex literals
# - Complex literals are numbers with a real and imaginary part
# - Complex literals can be written as a + bj, where a and b are real numbers
# - Complex literals can be written as a complex number

print(123j)
print(123 + 123j)
print(123 - 123j)
print(123 * 123j)
print(123 / 123j)

# List literals
# - List literals are lists of values enclosed in square brackets
# - List literals can be written as a list of values

print([1, 2, 3])
print([1, 2, 3, 4, 5])
print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Tuple literals
# - Tuple literals are tuples of values enclosed in parentheses
# - Tuple literals can be written as a tuple of values

print((1, 2, 3))
print((1, 2, 3, 4, 5))
print((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Dictionary literals
# - Dictionary literals are dictionaries of key-value pairs enclosed in curly braces
# - Dictionary literals can be written as a dictionary of key-value pairs

print({'a': 1, 'b': 2, 'c': 3})
print({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10})

# Set literals
# - Set literals are sets of values enclosed in curly braces
# - Set literals can be written as a set of values  

print({1, 2, 3})
print({1, 2, 3, 4, 5})
print({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

# Frozen set literals
# - Frozen set literals are frozen sets of values enclosed in curly braces
# - Frozen set literals can be written as a frozen set of values

print(frozenset({1, 2, 3}))
print(frozenset({1, 2, 3, 4, 5}))
print(frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))

