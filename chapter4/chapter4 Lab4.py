inputnum=int(input('구구단 몇 단을 계산할까?'))

print('구구단',inputnum,'단을 계산한다')

for i in range(1,10):
    resurt=inputnum*i
    print(inputnum,'*',i,'=',resurt)
else:
    print("구구단",inputnum,'단 계산완료')
