# Iterating through a list
ages = [56, 72, 24, 46]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print("Average age: ", average)

# Prints every letter except "e" in "Hello"
for letter in "Hello":
    if letter == "e":
        continue
    print("Letter: ", letter)

sum = 0
other_sum = 0
values = [2, 9, 1, 7]
for num in values:
    sum = sum + num
    other_sum += num
print("Sum of values: ", sum, other_sum)

for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
        print('*', end='')