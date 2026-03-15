# 범위:

def sum_all(start=0, end=100, step=1):
    output=0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))

#확인 문제 1
def f(x):
    return 2*x + 1

print(f(10))

#확인 문제 2
def mul(*values):
    output = 1
    for v in values:
        output *= v
    return output
print(mul(5, 7, 9, 10))

# 반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print(factorial(5))

# 재귀함수로 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# 재귀함수로 구현한 피보나치 수열
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))

# 메모: 딕셔너리를 사용해서 한번 계산한 값 저장
dictionary = {
    1: 1,
    2: 1
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
    
print("fibonacci(10):", fibonacci(10))
print("fibonacci(50):", fibonacci(50))

# 조기 리턴: 함수의 중간에 return이 있으면, 그 지점에서 함수가 종료된다.
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output
    
# 코드에 이름 붙이기
def number_input():
    output = input("숫자를 입력하세요: ")
    return float(output)
def get_circumference(radius):
    return 2 * 3.14 * radius

radius = number_input()
print(get_circumference(radius))

# 확인문제_리스트 평탄화
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output
example = [1, 2, [3, 4, 5], 6, [7, 8]]
print(flatten(example))

# 확인문제
"""
def 문제(남은사람수, 앉힌사람수):
    key = str([남은사람수, 앉힌사람수])
    # 종료 조건
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
         return 1
    # 재귀 처리
    count = 0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1):
        count += 문제(남은사람수 - i, i)
    # 메모화 처리
    memo[key] = count
    # 종료
    return count
"""

def print_n_times(value, n):
    for _ in range(n):
        print(value)

def sum_all(start=0, end=100, step=1):
    total = 0
    for i in range(start, end+1, step):
        total += i
    return total

def mul(*values):
    result = 1
    for v in values:
        result *= v
    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)




# 타입 힌트: 변수와 함수의 “의도된 타입”을 명시하는 문법
# 목적: 가독성 + 정적 분석

# 변수
age: int = 20
name: str = "jimin"

# 함수
def add(a: int, b: int) -> int: # -> int: int로 반환
    return a + b

print(add(3, 4))

# 자주 쓰는 타입들
list[int]
dict[str, int]
tuple[int, str]
set[str]