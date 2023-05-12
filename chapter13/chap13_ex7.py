import csv

with open('example2.csv', 'r') as csvfile:
     #example2.csv 파일을 csvfile 객체에 저장
    csvreader = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
    #숫자 데이터가 아닌 경우에만 묶고 묶지않은경우는 실수형으로 읽어오게됨
    #원본파일에 년도에 해당하는 데이터가 따옴표로 감싸져있지 않기에 묶이지않게 되었고
    #실수형으로 반환이 되었음 
    for row in csvreader:
        print(row)