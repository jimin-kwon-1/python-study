"""
02_math.py

NumPy 연산 이해하기
- 벡터 덧셈
- 벡터 곱셈
- 스칼라 연산
"""
import numpy as np

# 1 벡터 생성
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("x:", x)
print("y:", y)

# 2 벡터 덧셈
print("\n벡터 덧셈:", x + y)

# 3 벡터 곱셈 (요소별 곱)
print("요소별 곱:", x * y)

# 4 스칼라 곱
print("스칼라 곱:", x * 10)