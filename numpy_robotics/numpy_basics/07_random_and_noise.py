"""
랜덤 값 생성 + 노이즈 추가

로봇/센서/비전에서 필수
"""

import numpy as np

# 1 랜덤 배열 생성
# np.random.rand(m, n): 0 ~ 1 사이 균등분포
# 무작위 숫자 채우기
A = np.random.rand(2, 3)
print("랜덤 배열 A:")
print(A)

# 2 평균 0, 표준편차 1, 정규분포
# np.random.randn(m, n)
# 센서 노이즈 모델링 할 때
noise = np.random.randn(2, 3)
print("\n노이즈:")
print(noise)

# 3 데이터 + 노이즈
# 원래 값 A, 측정할 때 ±오차가 섞여서 data로 관측
data = A + noise * 0.1 # noise * 0.1: 노이즈의 흔들림 크기(표준편차) 줄이기
print("\n노이즈 추가된 데이터:")
print(data)

