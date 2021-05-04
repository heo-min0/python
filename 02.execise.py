# 2,4,6,8,10 값을 각각 제곱 한 값을 출력하라
for i in range(2,12,2):
    print(i*i)

# while 문을 이용하여 10에서 50까지의 짝수만 출력하라
w=10
while w<51:
    if w % 2 == 0:
        print(w)
    w+=1

# 0-9의 값을 for 문을 사용하여 하나씩 표시. 그러나 7이되면 루프를 종료
for i in range(10):
    print(i)
    if i == 7:break

# 0-9의 값을 하나씩 표시하라. 그러나 4의 경우는 표시하지 않는다. (continue를 사용)
for i in range(10):
    if i == 4:
        continue
    print(i)

# pass를 사용하여 0 ~ 9의 값을 하나씩 표시하라. 그러나 4의 경우는 표시하지 않는다
for i in range(10):
    if i == 4:pass
    else:print("pass",i)

# 1 ~ 10까지 목록에 저장하고 각각의 값을 제곱 한 값을 출력하라
    #listA = []
    #for i in range(1,11):
    #    listA.append(i)
listA = [i for i in range(1,11)]
for i in range(10):
    listA[i] = listA[i]**2
print(listA)
# 다음 dictionary 객체를 사용하여 각각의 key와 value를 가져오고 
# value가 20 이상인 경우 {key의 내용} : hot을 출력한다. 그 외의 경우 {key의 내용} : cold 출력하라
temperatures = { 'x': 24, 'y': 18, 'z': 30 }

for key,value in temperatures.items():
    print(key,value)

for key in temperatures:
    if temperatures[key] >= 20:
        print(key + ': hot')
    else :
        print(key + ': cold')

'''
목록 (결합)
변수 li1에 [1,2,3]목록을 대입 변수 li2에 [4,5]목록을 할당하고 두 목록을 결합하여 출력합니다.

출력 :[1,2,3,4,5]
'''
li1 = [1,2,3]
li2 = [4,5]
print(li1+li2)
'''
목록 (추가)
변수 목록 [1,2,3,4,5]을 할당하고이 목록의 끝 으로 6, 7하나씩 차례로 추가하십시오. 그 후, 최종 목록을 출력합니다.

출력 :[1,2,3,4,5,6,7]
'''
li3 = [1,2,3,4,5]
li3.extend([6,7])
print(li3)
'''
목록 (insert)
변수 목록 [1,2,3,4,5]을 만들고 0 번째와 1 번째 사이에 100 을 삽입하십시오.

출력 :[1,100,2,3,4,5]
'''
li4 = [1,2,3,4,5]
li4.insert(1, 100)
print(li4)





'''
정렬
변수 목록 [5,3,1,4,2]을 저장하고 오름차순으로 정렬 된 목록을 출력합니다.

출력 :[1,2,3,4,5]
'''
li5 = [5,3,1,4,2]
li5.sort()
print(li5)


'''
목록 (for 의한 조사)
변수에 [1,2,3,4,5] 5 개의 요소를 가진 리스트를 포함하여 짝수의 요소만을 출력합니다.

출력: 2 4
'''
li6 = [1,2,3,4,5]
for i in li6 : 
    if i % 2 == 0 : print(i)
'''
목록 (enumerate)
변수에 [1,2,3,4,5] 5 개의 요소를 가진리스트를 포함하여 짝수가 들어 있는 요소의 index만을 출력합니다. 

예상 출력 :1 3
'''
li7 = [1,2,3,4,5]
enu = enumerate(li7)
for i, val in enu:
    if val % 2 == 0 : 
        print(i)

'''
사전 (values)
변수에 값 쌍으로 {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}를 가진 사전을 포함하여 
키를 요소로 하는 리스트와 값을 요소로 하는 리스트를 작성하고 출력하십시오.

['A', 'B', 'C', 'D', 'E']
[1, 2, 3, 4, 5]
'''
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print( list(dic.keys()) )
print( list(dic.values()) )

'''
변수에 값 쌍으로 {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}를 가진 사전을 포함하여 
키와 값 (가치)의 조합 튜플을 요소로 하는 리스트를 작성하고 출력하십시오.

출력 :[('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]
'''
listB = []
for key in dic:
    tup = (key,dic[key])
    listB.append(tup)
print(listB)
