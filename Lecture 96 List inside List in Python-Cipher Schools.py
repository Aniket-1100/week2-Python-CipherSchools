matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2])
for i in matrix:
    for sublist in matrix:
        for i in sublist:
            print(i)

print(matrix[2][0])

s = "string"
print(type(s))