import csv

with open("trade_month.csv", 'r', encoding='cp949') as  trade_data: 
    #trade_month.csv 파일을 trade 객체에 저장
    data = csv.reader(trade_data)
    #csv 파일을 각 줄을 쉼표로 구분해 저장,따옴표로 구분된 데이터는 쉼표를 포함해 저장
    data_header = next(data) 
    #다음줄의 데이터를 반환하는 next()를 사용, 처음next는 첫줄을 반환함
    USA_only_rows = []
    #미국의 무역 데이터를 담을 빈 리스트 생성

    for row in data: 
        if row[1]=='미국':
        #2번째 인덱스는 국가명 칼럼임 국가명이 미국일때 True
                USA_only_rows.append(row)
        #미국의 USA_only_rows 리스트에 담음

    print('Header:', data_header)

    for i in range(5):
        print('Data' , i, USA_only_rows[i])
    