def matrix_addition(matrix_y,matrix_z):     # 행렬 덧셈
    result=[[sum(row) for row in zip(*i) ]for i in zip(matrix_y,matrix_z)]
    print(result)


matrix_y = [[2,5],[2,1]]

matrix_z= [[2,4],[5,3]]

for i in zip(matrix_y,matrix_z):          #작동방식 세부
    print(i)
    for row in zip(*i):
        print(row)

matrix_addition(matrix_y,matrix_z)

