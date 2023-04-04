ex=[1,2,3,4,5]
f=lambda x : x**2

print(list(map(f,ex)))

for value in map(f,ex):
    print(value)



ex=[1,2,3,4,5]                   #요즘은 람다함수로 안하고 리스트 컴프리헨션 으로 함
print([x**2 for x in ex])
