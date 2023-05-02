with open('dream.txt','r') as f:
    i=0
    while 1:
        line=f.readline()
        if not line:
            break
        print(str(i)+"==="+line.replace('\n',""))
        i=i+1