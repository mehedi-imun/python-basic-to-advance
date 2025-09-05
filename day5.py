matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[1][1])

# print(matrix[2][1]) 

# row wise 
# for row in matrix:
#     for value in row:
#         print(value,end=" ")
#     print(" ")

# Column-wise Traversal
# print(matrix[1][0])
# for c in range(len(matrix[0])):
#     for r in range(len(matrix)):
#         print(matrix[r][c],end=" ")
#     print() #1 




# Matrix Operations

for i,row in enumerate(matrix):
    print(sum(row))