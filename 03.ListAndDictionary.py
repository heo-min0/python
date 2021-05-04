#list, tuple
#list(추가, 삭제 가능) tuple(추가, 삭제 불가 대입용) 

[a,b] = [10,20] #list
(c,d) = (11,22) #tuple

print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)

tuple_test = (10,20,30)
print(tuple_test[0])

mylist = list(tuple_test) #tuple을 list로 변경후에는 값 변경 가능
mylist[0] = 100
print(mylist)


mylist = [23,56,12,34,'문자열',True,False]
print(mylist)
mylist[4] = 'world'

listA = [1,2,3]
listB = [4,5,6]
listC = listA + listB #합치기
print(listC)


listA.append(4) #맨 끝에 추가

listA.insert(1, 1.34) #중간에 추가

listA.extend([4,5,6]) #한꺼번에 추가

#삭제
del listA[1]

listA.pop(3)

del listA[2:4]
print(listA)

listA = [1,2,1,2,1,1]
listA.remove(2) # 처음부터 2의 값을 삭제(하나만)
print(listA)

listA.clear()

listA = [25,34,56,14,82]
print(56 in listA)

if 56 in listA:
    print('있음')

for i in listA:
    print(i)

for i in listA:
    if i == 34:
        print('값찾음')


listA.sort() # 오름차순
print(listA)
listA.sort(reverse=True) # 내림차순
print(listA)

#dictionary = hashMap = json
dic = {
    "name":"홍길동",
    "age":"24",
    "hobby":["독서","게임","스포츠"],
    "address":"서울시"
}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

print(dic['hobby'])
print(dic['hobby'][0]) #2차원배열

dic['name']='성춘향'
print(dic['name'])

dic['height']='175' #추가
print(dic)

del dic['address'] #삭제

if 'name1' in dic:
    print(dic['name'])
else:
    print('키값이 존재하지 않습니다.')

val = dic.get('age')
print(val)

val = dic.get('weight')
print(val) #에러가 아닌 none이 나옴

for key in dic:
    print(key, ":", dic[key])




