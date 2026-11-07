# finding in lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("a" in letters) # True

list1 = [0, 3, 4, 1, 2]
list1[2:5] = [8, 9]
list1.append(9)
print(list1)
print(list1.index(9)) # [0, 3, 8, 9, 2]