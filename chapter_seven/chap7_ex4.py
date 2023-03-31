def sort_by_key(t):
    return t[0]


from collections import OrderedDict

d=dict()

d['x']=100
d['y']=90
d['z']=600
d['l']=500

print(d.items())

print(sorted(d.items(),key=sort_by_key)) # d안에 있는 키값과 밸류값을 모두 출력해 정렬하는데 기준은  문자 만약 sort_by 함수에서 리턴값을 t[1] 로 한다면 밸류 값으로 정렬함 [키,밸류] 구성이니


for k,v in OrderedDict(sorted(d.items(),key=sort_by_key)).items():
    print(k,v)
