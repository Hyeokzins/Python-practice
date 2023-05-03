import random
answer=random.randint(1,10)
def guess_number(answer):
    try:
        guess=int(input('숫자를 넣어주세요:'))
        if answer == guess:
            print('정답')
        else:
            print('틀렸음')
    except ValueError:
        print('숫자가 아닙니다')
guess_number(answer)                  ##문자입력하는경우 guess에 문자들어가고 answer(정수)와 비교하게되어 ValueError일으켜서 숫자가 아닙니다가 뜸
