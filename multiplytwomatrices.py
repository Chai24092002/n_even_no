A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("A"A)
print("B",B)
# Multiply matrices
result = [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]

# Print result
for row in result:
    print(row)
