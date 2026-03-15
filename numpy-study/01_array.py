"""
01_array.py
NumPy 기본 개념 정리
- ndarray란?
- 리스트와 차이
- shape
- dtype
"""

# NumPy: 벡터, 행렬 계산을 위해 만들어진 라이브러리

# ndarray = n-dimensional array (n차원 배열)

# 1. 리스트 vs NumPy 배열
import numpy as np
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print("리스트:", python_list)
print("넘파이 배열:", numpy_array)
print("타입:", type(numpy_array))

# 2. 2차원 배열 (행렬)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\n행렬:")
print(matrix)

print("shape:", matrix.shape) # (2, 3) 2행 3열
print("dtype:", matrix.dtype) # int64 (NumPy는 모든 요소 타입이 동일해야 함)
# 기본 배열 만들기
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

# 2차원 배열
b = np.array([[1, 2, 3],
              [4, 5, 6]]) # 2행 3열

print(b)
print(b.shape) # (2, 3)
# shape(행, 열)

# 연산 차이 보기
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)
print(x * y)