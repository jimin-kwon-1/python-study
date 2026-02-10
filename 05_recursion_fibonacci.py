# 범위:
# 피보나치 재귀
# 메모이제이션

counter = 0

def fibonacci(n):
    global counter
    counter += 1
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

dictionary = {1:1, 2:1}

def fibonacci_memo(n):
    if n in dictionary:
        return dictionary[n]
    dictionary[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return dictionary[n]
