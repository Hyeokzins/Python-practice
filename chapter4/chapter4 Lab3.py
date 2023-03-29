year=int(input('당신이 태어난 연도를 입력하세요:'))

age=(2023-year+1)

if age<=26 and age>=20: print("당신의 나이는" ,age ,"살이니 대학생이군요")

elif age<20 and age>=17: print("당신의 나이는" ,age ,"살이니 고등학생이구만")

elif age<17 and age>=14: print("당신의 나이는" ,age ,"살이니 중학생이네")

elif age<14 and age>=8: print("당신의 나이는" ,age ,"살이니 초등학생이구나")

else: print("당신의 나이는" ,age ,"살이니 당신은 학생이 아닙니다")

