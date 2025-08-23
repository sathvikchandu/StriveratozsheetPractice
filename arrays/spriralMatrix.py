def print_spriral(matrix):
    n=len(matrix)
    m=len(matrix[0])


    top=0
    left=0
    right=m-1
    bottom=n-1

    while top<=bottom and left<=right:

        for i in range(left, right+1):
            print(matrix[top][i],end=" ")
        top+=1

        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")
        
        right-=1

        if (top<=bottom):
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
        bottom-=1

        if left<=right:
            for i in range (bottom,top-1,-1):
                print(matrix[i][left],end=" ")
        left+=1
spital_data=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print_spriral(spital_data)