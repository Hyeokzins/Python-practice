def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

asterisk_test(1,*(2,3,4,5,6)) # asterisk_test(1,2,3,4,5,6)



a,b,c=([1,2],[3,4],[5,6])
print(a,b,c)

data=([1,2],[3,4],[5,6])
print(data)
print(*data)