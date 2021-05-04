'''
try:
    number = int(input('정수입력>'))
    print('원의 반지름:',number)
    print('원주:',2*3.141592*number)
except:
    print('예외발생')
'''
listA = ['52','273','32','문자열','103']

listNumber = []

for item in listA:
    try:
        float(item)
        listNumber.append(item)
    except:
        # print('예외발생') 이셉션은 에러가 아니다
        pass

print('{}'.format(listA))
print('{}'.format(listNumber))

try:
    number = int(input('정수입력>'))
except Exception as exc:
    print('type:',type(exc))
    print(exc)
    print('정수 입력하셔야 함')
else: # 이셉트가 없을때는 사용 못 함
    print('예외가 발생 안함')
    print('원주:',2*3.141592*number)
finally:
    print('프로그램 종료')
