u=[2,2]
v=[2,3]
z=[3,5]

result=[sum(t) for t in zip(u,v,z)]
print(result)


def vector_addition(*args):
    print(*args)
    return [sum(t) for t in zip(*args)]

row_vectors=[[1,2],[2,3],[3,5]]
print(vector_addition(*row_vectors))