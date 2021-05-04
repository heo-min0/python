#txt, csv파일 토큰이 컴마, excel, 덧씌워지니 주의

file = open('basic.txt','w')

file.write('hello python programming')
file.close()
'''
fileDate = open('basic.txt')
data = fileDate.read()
print(data)
fileDate.close()
'''
#안에 처리로 묶어 둬야 할 때
with open('basic.txt', 'r') as file:
    content = file.read()
    print(content)

#close()를 호출 안해도 된다


import random

hanguls = list('가나다라마바사아자차카타파하')
with open('info.txt','w') as file:
    for i in range(1000):
        name = random.choice(hanguls)+random.choice(hanguls)
        weight = random.randrange(40,100) # 40 ~ 100-1
        height = random.randrange(140,200)

        file.write('{},{},{}\n'.format(name, weight, height))

with open('info.txt','r') as file:
    for line in file:
        (name, weight, height) = line.strip().split(',')

        #데이터가 문제 있는지 체크
        if (not name) or (not weight) or (not height) :
            continue
        
        h = int(height)/100
        bmi = int(weight) / h**2
        result = ''
        if 25 <= bmi:     result = '과체중'
        elif 18.5 <= bmi: result = '정상체중'
        else :            result = '저체중'

        print('\n'.join(['이름:{}','몸무게:{}','키:{}','BMI:{}','결과:{}']).format(name,weight,height,bmi,result))
        print()
