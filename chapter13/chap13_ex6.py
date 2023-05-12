import csv

with open('example1.csv', 'r') as csvfile:
    #example1.csv 파일을 csvfile 객체에 저장
    csvreader = csv.reader(csvfile, delimiter='|' ,quotechar='%')
    #csvfile 을 불러오는데 이때 데이터를 분리하는 기준은|로 분리해서 저장
    #단 %로 감싸져있는것은 묶어서 처리
    for row in csvreader:
        print(row)