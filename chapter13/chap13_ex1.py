line_counter=0 #파일의 총 줄 수를 세는 변수
data_header=[] # 데이터의 필드값을 저장하는 리스트
trade_list=[] #trade의 개별 리스트를 저정하는 리스트

with open("trade_month.csv",encoding='cp949') as trade:  
    #trade_month.csv 파일을 trade 객체에 저장
    while 1:
        data=trade.readline() 
        #trade_month.csv의 데이터 변수에 한줄씩 저장

        if not data:break #데이터가 없을시 반복문 종료
        if line_counter == 0: 
            # 첫번째 데이터들은 데이터의 필드(카테고리,열)
            data_header=data.split(',') #를 헤더 리스트에 따로 저장
        else:
            trade_list.append(data.split(',')) 
            #나머지 데이터들은 일반 trade_list 에 저장 
        
        line_counter += 1   
        #라인 카운터를 1을 증가시키며 line_counter == 0: 가 더이상 작동안하게 함
print('Header: ',data_header)   #데이터 필드값을 먼저 출력
for i in range(0,5):  # 데이터 5개만 출력
    print('Data',i,':',trade_list[i])
print(len(trade_list)) #총 데이터수 를 출력



