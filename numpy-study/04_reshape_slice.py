"""
배열 모양 바꾸기 + 슬라이싱
"""

import numpy as np

# 1 1차원 배열
a = np.array([1, 2, 3, 4, 5, 6])
print("a:", a)

# 2 reshape
b = a.reshape(2, 3) # 6개의 데이터를 2행 3열로 재배치
print("\nreshape 결과:")
print(b)
print("shape:", b.shape)

# 3 슬라이싱
# b[행, 열]
print("\n첫 번째 행:", b[0]) # b[0] 첫 행
print("첫 번째 열:", b[:, 0]) # b[:, 0] 모든 행 & 0번째 열 = 첫 열
