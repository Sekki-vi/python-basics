# Lists are ordered and mutable collections of items
countries = ["India", "USA", "Canada", "UK", "Australia"]
 # list is mutable, so we can change the value of the list by index
countries[0] = "Japan"

print(countries)

# del is used to delete the value of the list by index
del countries[1]

print(countries)

countries = ["India", "USA", "Canada", "UK", "Australia"]

print(countries[-1]) # print the last value of the list

print(countries[::3]) # print the values of the list from index 0 to last index with step 3
print(countries[:3]) # print the values of the list from index 0 to 2
print(countries[3:]) # print the values of the list from index 3 to last index
print(countries[1:3]) # print the values of the list from index 1 to 2
print("!",countries[0:1:1]) # print the value of the list from index 0 to 1 with step 1
print(countries[::-1]) # print the values of the list in reverse order
print(countries[::-2]) # print the values of the list in reverse order with step 2
print(countries[::-3]) # print the values of the list in reverse order with step 3
print(countries[::-4]) # print the values of the list in reverse order with step 4
print(countries[::-5]) # print the values of the list in reverse order with step 5
print(countries[::-6]) # print the values of the list in reverse order with step 6
