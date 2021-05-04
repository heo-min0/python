# 1) 임의의 0 ~ 100 사이의 숫자를 10 개 생성 목록에 저장하라
# 2) 각각의 값을 제곱하여 출력하라
import random
listA = [random.randint(0,100) for i in range(10)]
'''
listA = []
for i in range(10) :
    listA.append(random.randint(0,100))
'''
print(listA)
for i in listA :
    print(i*i)
'''
가위 바위 보하는 프로그램 
계산기와 가위 바위 보를하는 프로그램을 작성해 보겠습니다. 
가위 바위 보를 각각 0,1,2의 정수로 표현합니다. 
당신은 입력으로 입력하게 합니다. 컴퓨터는 난수(동일한 확률로 마구 수를 자동으로 생성하는 방법)을 사용하여 생성합니다. 
구체적으로는 random.randint(최소값, 최대 값) 수식을 사용하면 자동으로 최소값에서 최대 값까지 터무니없는 정수를 만들어줍니다. 
(프로그램의 시작에 'import random'의 선언이 필요)
comp = random.randint(0,2)
이렇게하면이 comp 0 또는 1 또는 2의 정수가 할당됩니다. 
입력한 당신의 숫자와 com을 비교하여 가위 바위 보 승부를 할 수있는 프로그램을 만드십시오.

가위 바위 보
당신은? (0 : 바위 1 : 가위, 2 : 보)> 1
당신은 가위. com은 보. 당신의 승리입니다.
'''
user = int(input('당신은? (0 : 바위 1 : 가위, 2 : 보)>'))
comp = random.randint(0,2)
print(comp)

u=''
if user == 0 : u='바위'
elif user == 1 : u='가위'
elif user == 2 : u='보'

c=''
if comp == 0 : c='바위'
elif comp == 1 : c='가위'
elif comp == 2 : c='보'

ma = user-comp

result = ""
if ma == 0 : #무
    result = '무승부'
else:    
    if ma < 0 :
        ma+=2
    if ma % 3 == 1 : #승
        result = '당신의 승리'
    elif ma % 3 == 0 : #패
        result = '당신의 패배'

print('당신은 {}. com은 {}. {}입니다.'.format(u,c,result))
