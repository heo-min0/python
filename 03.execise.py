
# add라는 함수를 정의하고 함수에서 5와 10을 더한 결과를 출력하도록하라.
def add(a,b):print(a+b)
add(5,10)
# add 함수의 인수가 숫자가 아닌 경우에 예외를 발생시킬 수 있기 때문에 그 경우는 0을 반환하라
try:add(12,sdfg)
except:print(0)

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성하라.
def avg(*a):
    sum = 0
    for i in a:
        sum+=i
    print(sum/len(a))
avg(2,3,4,5,5,6,7)
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
#(저장 문자열은 "java")
#with open('test.txt','a') as file: a는 추가
with open('test.txt','w') as file:
    file.write('java')
with open('test.txt','r') as file:
    for line in file:
        print(line)

# 저장한 test.txt 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

with open('test.txt','r') as file:
    for line in file:
        if line == 'java':
            with open('test.txt','w') as file:
                file.write('python')
   

