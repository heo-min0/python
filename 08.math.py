import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))

print(math.floor(2.5)) #내림
print(math.ceil(2.5))  #올림
#반올림할 자리의 수가 5이면 앞자리가 짝수면 내림, 홀수면 올림
print(round(1.5))

print(round(3.1415,2))
print(round(31.415,-1))

import random

print(random.random()) # 0.0 <= ~ < 1.0

#uniform
print(random.uniform(10, 20))
print(random.randrange(10)) # 0~9
print(random.randrange(1,5)) # 1~4
print(random.randint(1,5)) # 1~5

print(random.choice([11,33,5,7,9]))

#shuffle
listA = [1,2,3,4,5]
random.shuffle(listA)
print(listA)

#sample 이 중에서 몇개 고를 수 있음
print(random.sample([1,2,3,4,5], k=5)) 




