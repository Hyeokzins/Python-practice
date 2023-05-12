import csv

with open('example2.csv', 'r') as csvfile:
     #example2.csv 파일을 csvfile 객체에 저장
    csvreader = csv.reader(csvfile,quoting=csv.QUOTE_NONE)
    #데이터를 묶는 작업을 하지않음 쉼표만구분함
    for row in csvreader:
        print(row)