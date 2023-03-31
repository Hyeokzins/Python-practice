from collections import defaultdict

s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]

d=defaultdict(list)    #밸류는 리스트의 형태로 저장한다는뜻

for k,v in s:     #리스트 s의 key와 value를 차례대로 받아옴


    d[k].append(v)    ## s의 키와 밸류를 default 딕셔너리에 키와 밸류에 넣는데 이때 밸류는 리스트형태로 들어간다 
                      ## 리스트 s에는 동일한 키 값이 있고 밸류값이 다른 케이스가 있다 키값이 같아도 무조건 밸류는 리스트에 들어가기게 yellow,[1,3 ]형태로 나올것

print(d.items())

