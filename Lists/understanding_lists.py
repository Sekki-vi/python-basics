name = "Lydia"
ages = [56, 72, 24, 46]
# ages2 is a reference to the same list as ages
ages2 = ages
ages[0] = 92
print(ages2[0])

list1 = [1, 2, 3, 4]
# enumerate is a built-in function that returns the index and the value of the list
for i, j in enumerate(list1):
    print(i, j)

