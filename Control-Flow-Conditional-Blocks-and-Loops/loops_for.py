for i in range(10):
    print("i is:", i)
# will print 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(2, 5):
    print("i is:", i)
# will print 2, 3, 4

for i in range(1, 10, 2):
    print("i is:", i)
# will print 1, 3, 5, 7, 9

# break statement will exit the loop
# continue statement will skip the current iteration and continue with the next iteration
for i in range(5):
    if (i == 2):
        break
    print("i is:", i)
# will print 0, 1 and break on 2

for i in range(5):
    if (i == 2):
        continue
    print("i is:", i)
# will print 0, 1, 3, 4

x = 'abcd'
for i in x:
    print(i)
    x.upper()
# will print a, b, c, d

for i in x:
    print(i.upper())
# will print A, B, C, D

