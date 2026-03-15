"""
브로드캐스팅 (Broadcasting)

서로 다른 shape의 배열을 자동으로 맞춰 연산하는 기능
"""
import numpy as np

# 1 기본 예시
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([10, 20, 30]) # 원소 3개 1차원 배열.

print("A:")
print(A)

print("\nB:")
print(B)

# 2 브로드캐스팅 덧셈
print("\nA + B:")
print(A + B)

# A shape: (2, 3)
# B shape: (3,) <- 튜플
# NumPy가 자동으로 B 확장: [[10, 20, 30]
#                         [10, 20, 30]]

C = np.array([[100],
              [200]])

print("\nC:")
print(C)

print("\nA + C:")
print(A + C)
# C.shape: (2, 1)
# [[100 100 100]
#  [200 200 200]]