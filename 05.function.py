
def func():
    print('func 호출')

func()

def funcRange(val, n):
    for i in range(n):
        print(val)

funcRange('안녕', 5)

#가변인수(인자)  가변인수는 맨 뒤에 사용
def funcRange1(n, *values):
    for i in range(n):
        for v in values:
            print(v)
        print()

funcRange1(3,'안녕','하이')

#default 인수
def funcRange2(value, n=3, a=3):
    for i in range(n):
        print(value)

funcRange2('안녕하세요',a=5)

def testfunc(a,b=10,c=100):
    print(a+b+c)
testfunc(b=2,c=3,a=1)

#return
def testfunc1():
    print('testfunc1 호출')
    return True

print( testfunc1() )

def testfunc2(): #void형 함수
    print('testfunc2 호출')
    return
    print('testfunc2 내용처리')

#return 값을 다수
def testReturn():
    return (10, 20)

a, b = testReturn()
print(a,b)

#함수를 여러번 호출 가능
def myfunc():
    print('myfunc 호출')
    
def call10Func(_func): #함수 포인터? 주소값을 사용한다고 본다
    for i in range(10):
        _func()

call10Func(myfunc)

#modul 또는 라이브러리(Library)(dll) 정적과 동적의 차이
'''
import calculator as cal
result = cal.add(10, 3)
print(result)
print(cal.mul(10, 3))
'''

from calculator import div
d = div(3,2)
print(d)






