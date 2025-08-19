#my solution

matrix=[[1,1,1],[1,0,1],[1,1,1]]

temp_matrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            cooridinates=[i,j]
            temp_matrix.append(cooridinates)

for i in temp_matrix:
    matrix[i[0]]=[0]*len(matrix[0])
    for j in range(len(matrix)):
        matrix[j][i[1]]=0
print(matrix)

   

"""
ideal solution

def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row & col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero rows based on markers
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # Zero cols based on markers
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # Finally handle first row/col
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

"""
