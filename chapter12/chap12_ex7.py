while True:
    value=input('변환할 정수값을 입력해 주세요: ')
    for digit in value:
        if digit not in '0123456789':
            raise ValueError('숫자값을 입력하지 않았습니다.')
    print('정수값을 변환된 숫자 -', int(value))            