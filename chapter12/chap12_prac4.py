def sum_data(list_a,list_b):
    for i in list_a:
        for j in list_b:
            result=i+j
        return result
           # a리스트의 1+3 을했지만 다시 1+2로 초기화하고 a리스트의1의 관련된 것만 나옴 return 이 한칸 더밖에있었으면
    
a=[1,3]
b=[3,2]

print(sum_data(a,b))