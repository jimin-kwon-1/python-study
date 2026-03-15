# 08-1 클래스의 기본

# 객체 지향 프로그래밍 언어: 객체를 기반으로 프로그램을 만드는 프로그래밍 언어
# 객체: 데이터(속성)을 하나로 묶은 것 ex) 학생 한 명
# 추상화: 필요한 요소만을 사용해서 객체를 표현하는 것

# 딕셔너리로 객체 만들기
students = [ # 학생 리스트 선언 (객체들의 모음이자 객체)
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
]
print("이름", "총점", "평균", sep="\t") # 학생을 한 명씩 반복
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    #출력
    print(student["name"], score_sum, score_average, sep="\t")

# 딕셔너리 방식 단점: 키 오타나면 오류, 구조 고정되어있지 않음, 실수하기 쉬움, 매번 딕셔너리 직접 만들어야 함

# 객체를 만드는 함수(1)
def create_student(name, korean, math, english, science): # 딕셔너리를 리턴하는 함수 선언
    return{
        "name": name, 
        "korean": korean, 
        "math": math, 
        "english": english, 
        "science": science
    }

students = [ # 학생 리스트 선언
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t") # 학생을 한 명씩 반복
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")

# 객체를 처리하는 함수(2)
def create_student(name, korean, math, english, science): # 딕셔너리를 리턴하는 함수 선언
    return{
        "name": name, 
        "korean": korean, 
        "math": math, 
        "english": english, 
        "science": science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

students = [ 
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))

# 클래스: 객체를 만드는 설계도

# 클래스 선언하기
class Student():
    pass

student = Student() # 실제 객체 생성

# 인스턴스: 클래스로 실제로 만들어진 객체
# 인스턴스명(변수명) = 클래스명() <- 생성자 함수

# 붕어빵 틀: 클래스, 실체화된 붕어빵: 인스턴스

# 생성자: 클래스 이름과 같은 인스턴스를 생성할 때 사용하는 함수

# 클래스 내부에 __init__ 함수 만들면 객체 생성할 때 처리할 내용 작성 가능
# 생성자 역할: 객체가 만들어질 때 자동으로 그 안에 속성을 심어줌

#class 클래스 이름:
#    def __init__(self, 추가적인 매개변수):
#        pass

# self: 지금 만들어지고 있는 그 객체 자기 자신
# self가 가지고 있는 속성/기능에 접근할 때: self.식별자

class student:  # 클래스 선언
    def __init__(self, name, korean, math, english, science): # __init__: 생성자 메소드
        self.name = name # 이 학생 객체의 name 속성에 전달받은 name 값을 넣어라
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
students = [    # 학생 리스트 선언
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

# 소멸자
# 인스턴스가 소멸될 때 호출되는 함수
# 클래스 내부에 __del__(self) 형태로 함수 선언
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

test = Test("A")

# 메소드
# 클래스가 가지고 있는 함수. 객체의 속성을 이용해서 동작하는 함수

# class 클래스 이름:
#   def 메소드 이름(self, 추가적인 매개변수):
#       pass

# 클래스 내부에 함수(메소드) 선언하기
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name, 
            self.get_sum(), 
            self.get_average())
# 학생 리스트 선언    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())

# 08-2 클래스의 추가적인 구문

# 상속
# isinstance(): 객체(인스턴스)가 어떤 클래스로부터 만들어졌는지 확인
# isinstnace(인스턴스, 클래스)

class Student:  # 클래스 선언
    def __init__(self):
        pass

student = Student() # 학생 선언
print("isinstance(student, Student):", isinstance(student, Student))    # 인스턴스 확인 True/False

# isinstance() 함수 활용
class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:    # 반복문으로 적절한 함수 호출
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

# 특수 메소드
# __이름__()

# __str__() 함수: 객체를 print할 때 실행됨
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name, 
            self.get_sum(), 
            self.get_average())
    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student)) # str() 함수의 매개변수로 넣으면 student의 __str__() 함수 호출됨

# 크기 비교 함수

# eq: 같다
# ne: 다르다
# gt: 크다
# ge: 크거나 같다
# lt: 작다
# le: 작거나 같다

# 크기 비교 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)

# 클래스 변수와 메소드

# 클래스 변수
# : 모든 객체가 공유

# class 클래스 이름:
#   클래스 변수 = 값

# 클래스 변수에 접근 => 클래스 이름.변수 이름

class Student:
    count = 0 # 클래스 변수

    def __init__(self, name, korean, math, english, science): # 객체가 만들어질 때 자동으로 실행
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))
# 클래스 내부와 외부에서 클래스 변수에 접근할 때는 모두 Student.count 형태(클래스이름.변수이름)를 사용

# 클래스 함수: 클래스가 가진 함수

# 데코레이터: @classmethod 부분
# 기존 함수 코드를 안 건드리고, 기능을 덧붙이는 방법
# 클래스 함수 만들기

# class 클래스 이름:
#   @classmethod
#   def 클래스 함수(cls, 매개변수):
#       pass

# 클래스 함수 호출하기=> 클래스 이름.함수 이름(매개변수)

# 클래스 함수
class Student:  # 클래스 선언
    count = 0   # 클래스 변수
    students = []

    # 클래스 함수
    @classmethod    # 객체용이 아니라 클래스 전체용이다 표시. Student.print() 가능
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def  get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
# 학생 리스트 선언
Student("윤인성", 87, 98, 88, 95),
Student("연하진", 92, 98, 96, 98),
Student("구지연", 76, 96, 94, 90),
Student("나선주", 98, 92, 96, 92),
Student("윤아린", 95, 98, 98, 98),
Student("윤명월", 64, 88, 92, 92),
Student("김미화", 82, 86, 98, 88),
Student("김연화", 88, 74, 78, 92),
Student("박아현", 97, 92, 88, 95),
Student("서준서", 45, 52, 72, 78),

Student.print()

# 가비지 컬렉터: 더 이상 사용되지 않는 객체를 자동으로 메모리에서 제거하는 기능

# 가비지 컬렉터: 변수에 저장하지 않은 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))
Test("A")
Test("B")
Test("C")
# 변수에 저장돼지 않았으므로 바로 파괴

# 가비지 컬렉터: 변수에 저장한 경우
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다".format(self.name))

a = Test("A") # a가 A를 참조
b = Test("B") # b가 B를 참조
c = Test("C") # c가 C를 참조하므로 프로그램 종료 시점에 파괴

# 프라이빗 변수와 게터/세터

# 원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math # 모듈 가져오기

class Circle:   # 클래스 선언
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius**2)
    
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 프라이빗 변수: 클래스 내부의 변수를 외부에서 사용하는 것을 막을 때 __<변수이름>__
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10) # 객체 생성
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference()) 
print("원의 넓이:", circle.get_area())  # circle.get_area() => Circle.get_area(circle)가 동작. self = circle
print()
# __radius 에 접근
print("# __radius에 접근합니다.")
print(circle.__radius)

# 게터와 세터
# 프라이빗 변수의 값을 추출하거나 변경할 목적으로 간접적으로 속성에 접근하도록 해주는 함수
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    # 게터, 세터 선언
    def get_radius(self):   # 게터: 값을 “읽기” 위한 함수
        return self.__radius    # 세터: 값을 “수정”하기 위한 함수
    def set_radius(self, value):
        self.__radius = value

# 원의 둘레와 넓이
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

# 간접적으로 __radius 에 접근
print("# __radius에 접근합니다.")
print(circle.get_radius())
print()

# 원의 둘레와 넓이를 구합니다.
circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 게터 세터로 변수를 안전하게 사용하기
def set_radius(self, value):
    if value <= 0:
        raise TypeError("길이는 양의 숫자여야 합니다.")
    self.__radius = value

# 데코레이터를 사용한 게터와 세터
# @property: 게터 생성 (함수를 변수처럼 보이게 만드는 장치)
# @변수명.setter: 세터 생성
import math

class Circle:
    # ...생략...
    # 게터와 세터 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)  # # circle.radius => circle.radius() 가 동작
circle.radius = 2   # 내부적으로 radius(circle, 2) 가 동작
print("변경된 원의 반지름: ", circle.radius)    
print()

print("# 강제로 예외를 발생시킵니다.")
circle.radius = -10

# 상속: 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것
# class Child(Parent):
# Child가 Parent의 기능을 물려받는다
# 다중 상속
# 부모
# 자식

# 상속의 활용
class Parent:   # 부모 클래스 선언
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):    # 자식 클래스 선언
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")

child = Child() # 자식 클래스의 인스턴스 생성
child.test()    # 부모의 메소드 호출
print(child.value) # Parent의 __init__가 실행되면서 child 객체 안에 value라는 속성이 만들어진다
# child
# ├── value = "테스트"
# ├── test()  ← 부모에서 물려받음

# 예외 클래스 만들기

# 사용자 정의 예외 클래스 만들기
class CustomException(Exception): # Exception 클래스 상속
    def __init__(self):
        Exception.__init__(self)

raise CustomException   # 예외 발생시킴

# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("##### 내가 만든 오류가 생성되었어요! #####")
    def __str__(self):
        return "오류가 발생했어요"
    
raise CustomException # 오버라이딩 (부모 Exception 클래스에도 __str__ 존재)
# 재정의(오버라이드): 부모에 정의돼있는 함수를 자식에서 다시 정의하는 것

# 자식 클래스로써 부모에 없는 새로운 함수 정의하기
class CustomException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.mesage = message
        self.value = Value
    
    def __str__(self):
        return self.message
    
    def print(self):
        print("##### 오류 정보 #####")
        print("메세지:", self.message)
        print("값:", self.value)
# 예외를 발생시켜 보기
try:
    raise CustomException("딱히 이유 없음", 273)
except CustomException as e:
    e.print()
    