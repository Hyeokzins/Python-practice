sentence=list('hello gachon')

while (len(sentence)+1):
    try:
        print(sentence.pop(0))
    except Exception as e:            #IndexError: pop from empty list 없는걸 팝하려니까 오류발생
        print(e)
        break

