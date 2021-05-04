
print('hello python')

print("test anaconda", end="")

print("test", "anaconda")

print() #개행

print("anaconda")

#한줄 주석문
'''
범위
'''

"""
'''범위'''
print("anaconda")
#"""

# modul <- library
import keyword

print(keyword.kwlist)

print('"안녕하세요"라고 말했습니다.')
print("'안녕하세요'라고 말했습니다.")
print("\"안녕하세요\"라고 말했습니다.")

print("이름\t나이\t지역")

#보이는데로 출력
print("""인터페이스 옵션은 인터프리터에 의해 소비되는 옵션의 목록을 종료합니다,
 뒤따르는 ... command 의 파이썬 코드를 실행합니다.
  command 는 개행 문자로 구분된 하나 이상의 ... 인자가 모듈 이름이기 때문에,
   파일 확장자( .py )를 주지 않아야 합니다. ... 스크립트가 첫 번째 인자로 전달되거나 -c 옵션이 사용되면, 
   sys.stdin 가 터미널로 ...""")

print("안녕하세요 " * 3)

print("안녕하세요 "[0])
print("안녕하세요 "[1])
print("안녕하세요"[-1])
print("안녕하세요 "[0:2])
print("안녕하세요 "[2:])
print("안녕하세요 "[:])
print("안녕하세요 "[:3])

#print("안녕하세요 "[6])

print(len("안녕하세요"))
print(type("안녕하세요"))

print(type(len("안녕하세요")))

print(type(123.4567))

print(5*7)
#print(5/0)

print("3/2=",3/2) # 나누기
print("3/2=",3//2) # 몫

print("3**2=",3**2) #제곱

str1 = "문자열"
number = 273
print(str1,number)

# web > django, flask   시각화(app, web)

#입력
#str = input("입력>")
print(str1)
print("자료형",type(str1))
#입력받은것은 무조건 문자열
#문자열을 숫자로
numstr = int("135")
fnumstr = float("123.456")

print(numstr+10, type(numstr))
print(fnumstr+1.2, type(fnumstr))

#숫자를 문자열로
strnum = str(52)
strfnum = str(52.345)

print(type(strnum))
print(type(strfnum))

#format() 함수 > 숫자를 문자열로

foutput = "{}".format(2345)
print(foutput,type(foutput))

f1 = "{}원".format(3000)
f2 = "{} {}".format(100,23)
f3 = "{} {} {}".format(12,"문자열",True)

print(f1)
print(f2)
print(f3)

str_a="hello Python Programig"
str_up = str_a.upper()
str_low = str_a.lower()

print(str_up)
print(str_low)

str_sp = str_a.split(" ")
print(str_sp)

#join
print("::".join(["1","2","3"]))

str_a = '''
    안녕하세요
    문자열 함수를 작성합니다.
    
'''
print(str_a)
print(str_a.strip()) # trim

#문자열을 조사, 영어 한글 숫자로만 되어있으면 true
print("TrainsA10한글".isalnum())
print("TrainsA10^한글".isalnum())
#문자열이 숫자인지 아닌지
print("10".isdigit())
#find, rfind
out_a = "안녕안녕하세요".find("안녕")
print(out_a)

out_a = "안녕안녕하세요".rfind("안녕")
print(out_a)

print(10==100)
print("가방"=="가방")
print("가방">"하마")

x=25
print( x>10 and x<30)
print( 10<x<30)


