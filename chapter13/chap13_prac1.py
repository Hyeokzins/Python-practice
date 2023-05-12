line_counter=0 #파일의 총 줄 수를 세는 변수
data_header=[] # 데이터의 필드값을 저장하는 리스트
housing_list=[] #housing의 개별 리스트를 저정하는 리스트

with open( "housing.csv") as houseing: 
    #"housing.csv"을 열고 houseing 이라고 칭함 

    while 1:
        data= houseing.readline() 
        #밑에 line_counter변수를 활용한것을 근거로
        #한줄씩읽어 오는 방법을 사용하는것으로 추측
        if not data:break 
        #데이터가 없을시 반복문 종료

        if line_counter == 0: 
            # 첫번째 데이터들은 데이터의 필드(카테고리,열)
            data_header=data.split(',') #를 헤더 리스트에 따로 저장
        else:
            housing_list.append(data.split(',')) 
            #위에 헤더 데이터들 쉼표로 구분하니 이후 데이터들도 
            #쉼표로 구분할것으로 예상
        
        line_counter += 1   
        #라인 카운터를 1을 증가시키며 line_counter == 0: 가 더이상 작동안하게 함

print(housing_list[1][0])
#housing_list의 2번째 행에 1번째 열값을 출력하라는 명령어




