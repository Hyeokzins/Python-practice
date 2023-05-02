a=list(range(5))

for i in range(10):
    try:
        print(a[i])

    except IndexError:
        print('index over')