#range( <시작 숫자>,<끝 숫자(-1)>,<증가 숫자>  ) 루프용으로 많이씀
#범위값을 가지는 것

print(range(5))  #0부터 5 전 까지
print(list(range(5))) #동적배열 0부터 4까지


print(list(range(5,10))) #for(int i = 5; i<10;i++)

print(list(range(0,10,2)))  #for(int i = 0; i<10; i=i+2)

for i in range(10):
    print(str(i)+"번째 수")

array = ['one','two','three','four','five'] 
for a in array:     #for(String a : array)
    print(a)

for i in range(5,10):
    print(i)

#list
array = [273,32,103,73,52]

for i in range(len(array)):
    print("{}번째 수:{}".format(i,array[i]))

#역반복문
for i in reversed(range(10)):
    print(i)

