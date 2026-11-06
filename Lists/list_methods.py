# List methods are used to perform operations on lists
countries = ["India", "USA", "Canada", "UK", "Australia"]

countries.append("Germany") # add a value to the end of the list

print(countries)

countries.insert(1, "Japan") # insert a value at a specific index

print(countries)

# swap the values of the list
# this is how you would do it in Java
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp

# Python makes it easier to swap the values of the list
countries[0], countries[1] = countries[1], countries[0]

countries.sort() # sort the list in ascending order

print("Sorted list in ascending order: ", countries)

countries.sort(reverse=True) # sort the list in descending order

print("Sorted list in descending order: ", countries)

countries.reverse() # reverse the list

print("Reversed list: ", countries)

countries.pop() # remove the last value from the list

print("List after pop: ", countries)

countries.pop(1) # remove the value at a specific index

print("List after pop: ", countries)
