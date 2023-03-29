inputnum=int(input('구구단 몇 단을 계산할까?'))
while (inputnum!=0):
    if not(inputnum>=1 and inputnum<=9):
        print('잘못입력했어 1~9단만 지원해')
        inputnum=int(input('구구단 몇 단을 계산할까?'))
        continue
    else:
        print('구구단',inputnum,'단을 계산한다')
        for i in range(1,10):
            resurt=inputnum*i
            print(inputnum,'*',i,'=',resurt)
        else:
            print("구구단",inputnum,'단 계산완료')
            inputnum=int(input('구구단 몇 단을 계산할까?'))
print('프로그램종료')



