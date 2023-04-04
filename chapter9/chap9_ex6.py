matrix_a=[[3,6],[4,5]]
matrix_b=[[5,8],[6,7]]

result=[ [sum(k) for k in zip(*t)] for t in zip(matrix_a,matrix_b)]

print(result)