# nested lists 2d
# matrix
classroom = [
    ["John", "Jane", "Jim", "Jill"],
    ["Tom", "Tim", "Tina", "Todd"],
    ["Harry", "Hank", "Hannah", "Holly"],
    ["Jack", "Jill", "Jim", "Jill"],
    ["John", "Jane", "Jim", "Jill"],
    ["John", "Jane", "Jim", "Jill"],
]

# Index by row, column
print(classroom[2][1]) # Hank

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = []

for submatrix in matrix:
    for value in submatrix:
        matrix2.append(value)

print(matrix2) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = []
for i in range(2):
    a.append([])
    for j in range(10):
        a[i].append(j)
print(a)

countries = [["China", "Japan", "Korea"], ["USA", "Canada", "Mexico"], ["France", "Germany", "Italy"]]
# list comprehension
# [expression for item in iterable if condition]
countries2 = [country for sublist in countries for country in sublist if len(country) < 6]
print(countries2) # ["China", "Japan", "Korea", "USA", "Italy"]

countries2 = []
for sublist in countries:
    for country in sublist:
        if len(country) < 6:
            countries2.append(country)
print(countries2) # ["China", "Japan", "Korea", "USA", "Italy"]

matrix = [[j for j in range(4)] for i in range(4)]
print(matrix)

matrix2 = []
for i in range(4):
    matrix2.append([])
    for j in range(4):
        matrix2[i].append(j)
print(matrix2)