'''
class Car:
    honk = '빵빵'

    def info(self, color, year):
        print('color: %s, year: %d' %(color, year))

myCar = Car()
print( myCar.honk )
myCar.info('빨강', 2021)
'''
# setter, getter
'''
class Car:
    def setInfo(self, color, year):
        self.color = color
        self.year = year

    def getInfo(self):
        print('color: %s, year: %d' %(self.color, self.year))

myCar = Car()
myCar.setInfo('파랑', 2022)
myCar.getInfo()
'''
# init() initialize
'''
class Car:
    def __init__(self,color,year):
        self.color = color
        self.year = year
        print('새로운 Car 인스턴스 생성')

    def getInfo(self):
        print('color: %s, year: %d' %(self.color, self.year))

myCar = Car('Green',2020)
myCar.getInfo()
'''

# 상속
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print('이름:'+self.name, '나이:',self.age)
        print('부모 클래스의 info')

person = Person('홍길동', 24)
person.info()

class Employee(Person):
    def info(self):
        print('자식 클래스의 info')

emp = Employee('일지매', 22)
emp.info()

# 변수(instance, clas)
class InstanceVar:
    def __init__(self):
        self.text_list = []

    def add(self,text):
        self.text_list.append(text)

    def printList(self):
        print(self.text_list)

iv = InstanceVar()
iv.add('tigers')
iv.add('lions')
iv.printList()

iv1 = InstanceVar()
iv1.add('twins')
iv1.printList()

class ClassVar:
    #def __init__(self):
    #    self.text_list = []
    text_list = [] # class 변수

    def add(self,text):
        self.text_list.append(text)

    def printList(self):
        print(self.text_list)

cv1 = ClassVar()
cv1.add('tigerns')
cv1.printList()

cv2 = ClassVar()
cv2.add('linos')
cv2.printList()

print( ClassVar.text_list )


class InstanceCounter:
    count = 0 # class 변수

    def __init__(self):
        InstanceCounter.count += 1
    
    @classmethod
    def print_count(cls):
        print(cls.count)

ic1 = InstanceCounter()
InstanceCounter.print_count()

ic2 = InstanceCounter()
InstanceCounter.print_count()

# super
class Parant:
    def __init__(self): # 생성자가 아닌 기본함수
        print('Parant.init')
        self.message = 'hello'

class Child(Parant):
    def __init__(self):
        print('Child.init')

        super().__init__() # 오버라이딩 된 메소드 호출은 슈퍼로 호출
        print(self.message) # 변수는 그냥 self 만 붙여서 호출

if __name__ == '__main__':
    child = Child()