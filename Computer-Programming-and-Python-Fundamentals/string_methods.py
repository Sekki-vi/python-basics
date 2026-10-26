# arithmetic operations can be performed on strings
# string multiplication is the same as repeating the string
print("ha" * 10)

# string addition is the same as concatenating the strings
print("ha" + "ha")

# type conversion is required to perform arithmetic operations on strings
cost_of_apple = 2
amount_of_apples = input("How many apples do you want to buy? ")
total_sum = cost_of_apple * int(amount_of_apples)
print("You have to pay: " + str(total_sum) + " dollars")

# Summary:
# with the + operator, we can concatenate strings
# with the * operator, we can repeat a string
# with the str() function, we can typecast a number into a string