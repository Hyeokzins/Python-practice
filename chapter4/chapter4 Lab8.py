score=[[49,80,20,100,80],[43,60,85,30,90],[49,82,48,50,100]]

avg=[]
for i in range(len(score[0])):
    sum=0.0
    for j in range(len(score)):
        select=score[j][i]
        sum=sum+select

    avg.append(sum/len(score))

    
print(avg)


   

