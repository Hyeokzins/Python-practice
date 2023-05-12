line_counter=0 #파일의 총 줄 수를 세는 변수
data_header=[] # 데이터의 필드값을 저장하는 리스트
trade_USA_only_list=[] 
#trade의 국가 칼럼에 미국인 자료들을 저정하는 리스트
trade=[]

with open("trade_month.csv",'r',encoding='cp949') as trade_data: 
     #trade_month.csv 파일을 trade 객체에 저장
    while 1:
        data=trade_data.readline() 
        #trade_month.csv의 데이터 변수에 한줄씩 저장

        if not data:break #데이터가 없을시 반복문 종료
        if line_counter == 0: 
            # 첫번째 데이터들은 데이터의 필드(카테고리,열)
            data_header=data.split(',') #를 헤더 리스트에 따로 저장
        else:
            trade=data.split(',')
            if trade[1]=='미국':
                trade_USA_only_list.append(trade)

        line_counter += 1   
        #라인 카운터를 1을 증가시키며 line_counter == 0: 가 더이상 작동안하게 함
print('Header: ',data_header)   #데이터 필드값을 먼저 출력
for i in range(0,5):  # 데이터 5개만 출력
    print('Data',i,':',trade_USA_only_list[i])
print(len(trade_USA_only_list)) #총 데이터수 를 출력



