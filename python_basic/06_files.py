# 범위:
# 파일 쓰기/읽기
# 랜덤 데이터 생성


# 파일 처리
## 파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)
## 파일 객체.close(): 파일 객체 닫기

file = open("basic.txt", "w") # 쓰기 모드로 파일 열기

file.write("Hello Python Programming...!") # 파일에 문자열 쓰기
file.close() # 파일 닫기

# with 키워드: 파일 자동 닫기
## with open(문자열: 파일 경로, 문자열: 읽기 모드) as 파일 객체:
##     문장
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming...!")

# 파일 객체.read(): 파일 전체 내용 읽기
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)

# 텍스트 한 줄씩 읽기
## 랜덤하게 1000명의 키와 몸무게 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트 쓰기
        file.write("{}, {}, {}\n".format(name, weight, height))

# for 한줄 나타내는 문자열 in 파일 객체:
#     처리

## 반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r") as file: 
    for line in file:
        (name, weight, height) = line.strip().split(", ") # 변수 선언
        if (not name) or (not weight) or (not height):
            continue # 데이터에 문제 있으면 건너뛰기
        bmi = int(weight)/((int(height)/100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()

# 제너레이터: 이터레이터를 직접 만들 때 사용하는 코드, 값을 한 번에 다 만드는 게 아니라 필요할 때 하나씩 만드는 함수
# 함수 내부에 yield 키워드 사용하면 제너레이터 함수 됨, 
# 함수 호출해도 함수 내부의 코드 실행 안 됨, next() 함수로 함수 내부 코드 실행
# next(): yield까지 실행

# yield: 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 뜻. 중간값 리턴 후 다음 함수가 종료되지 않고 맨 끝까지 실행됨
# (return: 함수 종료, yield: 멈춤)
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
print(next(g))
print(next(g))


def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
output = test() # 제너레이터 함수 호출
print("D 지점 통과")
a = next(output) # 제너레이터 내부 코드 실행
print("a:", a)
print("E 지점 통과")
b = next(output)
print("b:", b)
print("F 지점 통과")
c = next(output)
print("c:", c)
next(output) # 더 이상 yield 없으므로 StopIteration 예외 발생

# 확인문제1
numbers = [1, 2, 3, 4, 5, 6]
print("::".join(map(str, numbers))) # 리스트의 각 요소를 문자열로 바꿔서 "::"로 연결하여 출력

# 확인문제2
numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()

print("# 3 이상, 7 미만 추출하기")
print(list(filter(lambda x: x >= 3 and x < 7, numbers)))