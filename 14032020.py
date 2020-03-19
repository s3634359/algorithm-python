def reshape_matrix(mat, x, y):
  # Fill this in.
    values = []
    for row in mat:
        for element in row:
            values.append(element)
    if len(values) is not (x * y) :
        return None
    else :
        output = []
        a = 0
        for i in range(x):
            row = []
            for j in range(y):
                row.append(values[a])
                a += 1
            output.append(row)
        return output
        
print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1, 2, 3, 4]]

print(reshape_matrix([[1, 2], [3, 4]], 4, 1))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
