# 범위:
# def / return
# 기본값 / *args
# 재귀 / 튜플 / 람다

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

# tuple & unpacking
a, b = 10, 20
a, b = b, a

def test():
    return 10, 20

x, y = test()

# lambda / map / filter
numbers = [1,2,3,4,5]
print(list(map(lambda x: x*x, numbers)))
print(list(filter(lambda x: x < 3, numbers)))
