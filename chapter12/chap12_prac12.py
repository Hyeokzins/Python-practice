for i in range(3):
    try:
        print(i,3//i)
    except ZeroDivisionError:
        print("Not division by zero")