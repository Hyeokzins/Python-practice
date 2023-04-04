from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5]))


ex=[1,2,3,4,5]

print(list(map(lambda x :x**2 if x%2==0 else x,ex)))


