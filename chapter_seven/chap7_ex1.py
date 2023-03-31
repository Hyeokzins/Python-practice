s1=set([1,2,3,4,5])
s2=set([3,4,5,6,7])


a=s1.union(s2)
a1=s1|s2

print(a)
print(a1)

b=s1.intersection(s2)

b2=s1&s2

print(b)
print(b2)


c=s1.difference(s2)   #차집합 s1과s2의 교집합을 s1에서 뺀것
c1=s1-s2

print(c)
print(c1)
