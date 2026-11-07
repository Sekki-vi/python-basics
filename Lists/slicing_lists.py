# Slicing Lists
# list[start:end:step]

my_list = [1, 2, 3, 4, 5]
print(my_list[1:3]) # [2, 3]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:3]) # [1, 2, 3]
print(my_list[::2]) # [1, 3, 5]
print(my_list[::-1]) # [5, 4, 3, 2, 1]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
firstTwo = letters[0:2]
print(firstTwo) # ['a', 'b']
print(letters[1:]) # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[1:-1]) # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# slicing a list creates a new list in memory
original_list = [1, 2, 3, 4, 5]
new_list = original_list[1:3]
print(new_list) # [2, 3]
print(original_list) # [1, 2, 3, 4, 5]
print(id(original_list)) # 140735121314816
print(id(new_list)) # 140735121315136

# cal also delete from list
del original_list[1:3]
print(original_list) # [1, 4, 5]

print(original_list[1:2])