import csv

with open("trade_month.csv", 'r', encoding='cp949') as  trade_data: 
    #trade_month.csv 파일을 trade_data 객체에 저장
    data = csv.reader(trade_data)
    #디폴트 값으로 csv 파일을 각 줄을 쉼표로 구분해 저장, 따옴표로 구분된 데이터는 쉼표를 포함해 저장
    data_header = next(data) 
    #다음줄의 데이터를 반환하는 next()를 사용, 처음next는 첫줄을 반환함
    rows = [] 
    #각행의 데이터를 담을 빈 리스트 생성

    for row in data: 
        rows.append(row)
        #각행의 데이터를 rows 리스트에 담음

    print('Header:', data_header)

    for i in range(5):
        print('Data' , i, rows[i])
    