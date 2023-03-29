import random

num=random.randrange(1,100)

answer=int(input("숫자를 맞추어 보세요 1~100"))

while True:
    if answer==num:
        print('정답입니다 입력한 숫자는 ',answer,'입니다  프로그램을 종료합니다')
        break
    elif answer<num:
        answer=int(input("숫자가 너무 작습니다 다시입력하세요"))

    elif answer>num:
        answer=int(input("숫자가 너무 큽니다 다시입력하세요"))
