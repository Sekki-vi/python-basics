# nested lists 3d
school = [
    [
        ["John", "Jane", "Jim", "Jill"],
        ["Sarah", "Sam", "Sue", "Sally"],
        ["Mike", "Mia", "Moe", "Molly"],
        ["Bob", "Betty", "Bill", "Bobby"],
    ],
    [
        ["John", "Jane", "Jim", "Jill"],
        ["Sarah", "Sam", "Sue", "Sally"],
        ["Mike", "Mia", "Moe", "Molly"],
        ["Bob", "Betty", "Bill", "Bobby"],
    ],
    [
        ["John", "Jane", "Jim", "Jill"],
        ["Sarah", "Sam", "Sue", "Sally"],
        ["Mike", "Mia", "Moe", "Molly"],
        ["Bob", "Betty", "Bill", "Bobby"],
    ],
    [
        ["John", "Jane", "Jim", "Jill"],
        ["Sarah", "Sam", "Sue", "Sally"],
        ["Mike", "Mia", "Moe", "Molly"],
        ["Bob", "Betty", "Bill", "Bobby"],
    ]
]
 
# index by floor, room, student
# index by matrix, row, column (z, y, x)

student = school[1][2][1]
print(student) # Mia

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)

matrix2 = []
for i in range(3):
    matrix2.append([])
    for j in range(3):
        matrix2[i].append([])
        for k in range(3):
            matrix2[i][j].append(k)
print(matrix2[0][0][1])