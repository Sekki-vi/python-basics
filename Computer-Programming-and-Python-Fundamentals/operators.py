# Python has 7 types of arithmetic operators
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Floor division (//)
# 6. Modulus (%)
# 7. Exponentiation (**)

# Addition
print(1 + 1)
print(1.0 + 1.0)
print(1.0 + 1)
print(1 + 1.0)

# Exponentiation
# If one value is a float, the result will be a float
# If both values are integers, the result will be an integer
print(2 ** 3)
print(2. ** 3.)
print(2 ** 3.)
print(2. ** 3)

# same for multiplication
print(2 * 3)
print(2. * 3.)
print(2. * 3)
print(2 * 3.)

# division is always a float
print(2 / 3)
print(2. / 3.)
print(2. / 3)
print(2 / 3.)

# floor division return a whole number as an integer or float
print(2 // 3)
print(2. // 3.)
print(2. // 3)
print(2 // 3.)

# modulus returns the remainder of the division
print(4 % 2)
print(5 % 2)

# can choose sign inline with - or +
print(-4 % 2)

# even in addition and subtraction
print(1 - -2)
print(1 + -2)

# same for multiplication
print(1 * -2)
print(1 * -2)

# same for division
print(1 / -2)
print(1 / -2)

# - can  be be binary or unary

# we can use as many operators as we want in an expression
print(1 + 2 * 3 - 4 / 5 ** 6 % 7 // 8)
print(1 + 2 * 3 - 4 / 15625 % 7 // 8)
print(1 + 6 - 4 / 15625 % 7 // 8)
print(1 + 6 - 0.000256 % 7 // 8)
print(1 + 6 - 0.000256 // 8)
print(1 + 6 - 0)
print(7 - 0)
print(7)
# Answer is 7.0

# we can use parentheses to group expressions
print(1 + (2 * 3) - (4 / 5) ** (6 % 7) // 8)
# Answer is 7.0

# order of operations is important. Follows PEMDAS rule
# Parentheses
# Exponents
# Multiplication and Division (from left to right)
# Addition and Subtraction (from left to right)
