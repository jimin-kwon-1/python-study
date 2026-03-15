"""
NumPy 통계 함수 + axis 개념
"""

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
# shape = (2, 3)

print("A:", A)

# 1 전체 합
print("\n전체 합:", np.sum(A))

# 2 행 기준 합 (axis = 1)
# 가로 방향을 따라 연산 (행끼리 연산)
# [1+2+3, 4+5+6] = [6, 15]
print("행 기준 합:", np.sum(A, axis=1))

# 3 열 기준 합 (axis = 0)
# 세로 방향을 따라 연산 (열끼리 계산)
# [1+4, 2+5, 3+6] = [5, 7, 9]
print("열 기준 합:", np.sum())

# 4 평균
print("\n전체 평균:", np.mean(A))
print("행 평균:", np.mean(A, axis=1))
print("열 평균:", np.mean(A, axis=0))

# keepdims: shape 유지
np.sum(A, axis=1, keepdims=True)