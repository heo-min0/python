
number = 12

if number > 0:
    print("0보다 크다")

if number < 10:
    print("10보다 작다")

if number == 0:
    print("0입니다")

#날짜 시간 취득
import datetime

#현재 날짜/시간
now = datetime.datetime.now()
print(now.year,'년')
print(now.month,'월')
print(now.day,'일')
print(now.hour,'시')
print(now.minute,'분')
print(now.second,'초')

if now.hour < 12:
    print('현재시간은 {}시로 오전입니다.'.format(now.hour))

if now.hour >= 12:
    print('현재시간은 {}시로 오후입니다.'.format(now.hour))

#시간설정
setTime = datetime.datetime.strptime('2021-05-06 12:35:45', '%Y-%m-%d %H:%M:%S')
print(setTime)

#시간변경
setTime = setTime.replace(year=2022)
setTime = setTime.replace(hour=18)
print(setTime)

#계절구분
if now.month >= 3 and now.month <= 5:
    print('이달은 {}월로 봄입니다.'.format(now.month))

if 3 <= now.month <= 5:
    print('이달은 {}월로 봄입니다.'.format(now.month))

number = 245
if number % 2 != 0:
    print('홀수입니다.')

month = datetime.datetime.now().month

if 3 <= month <= 5:
    print('봄입니다.')
elif 6 <= month <= 8:
    print('여름입니다.')
elif 9 <= month <= 11:
    print('가을입니다.')
else :
    print('겨울입니다.')

#pass
number = int( input('정수입력 >') )
if number > 0:
    pass #미구현
else:
    pass #미구현

if number > 0:
    raise NotImplementedError #에러 강제로 일으킴
else:
    raise NotImplementedError




