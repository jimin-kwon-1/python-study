"""
03_matrix.py

행렬과 관련된 핵심 개념
- 2차원 배열
- 전치 (transpose)
- 행렬곱
"""
import numpy as np

# 1 행렬 만들기
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("A:\n", A)
print("B:\n", B)

# 2 전치 (Transpose)
print("\nA의 전치:")
print(A.T)

# 3 요소별 곱
print("\n요소별 곱:")
print(A * B)

# 4 행렬곱
# ( m × n ) @ ( n × p ) = ( m × p ) 안쪽 숫자 같아야 함
print("\n행렬곱:")
print(A @ B) # 또는 np.dot(A, B)

# 요소별 곱, 행렬곱 차이
# A * B => 자리별로 곱
# A @ B => 선형대수학 행렬곱
