try:
    for i in range(1,7):
        result = 7//i
        print(result)
except ZeroDivisionError:
    print('not division by zero')    #발생할 일이 없음
finally:
    print('종료')