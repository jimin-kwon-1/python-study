"""
14_matrix_multiplication_order.py

행렬곱의 적용 순서 정리

핵심 개념:
행렬곱 A @ B 는
"B가 먼저 적용되고, 그 다음 A가 적용된다."

A @ B = 먼저 B, 그 다음 A
--------------------------------------------
왜 그런가?

열벡터 기준 수학 공식:
p' = A @ B @ p

계산 순서:
(1) 먼저 B @ p
(2) 그 결과에 A 적용

그래서 B가 먼저 적용된다.
--------------------------------------------
행벡터 방식 (NumPy에서 사용하는 방식)

p' = p @ (A @ B).T

전치 규칙:
(A @ B).T = B.T @ A.T

따라서 실제 적용 순서는:
- 먼저 B
- 그 다음 A
--------------------------------------------
⚠️ 중요한 점

행렬곱은 교환법칙이 성립하지 않는다.

A @ B ≠ B @ A

순서를 바꾸면 완전히 다른 변환이 된다.

변환 순서 예시
   회전 후 이동을 하고 싶다면:
       T_total = T_translate @ R_rotate

   이유:
   - R_rotate 가 먼저 적용
   - 그 다음 T_translate 적용
--------------------------------------------
실험 코드
"""

import numpy as np

# 원래 점 (3D)
point = np.array([[1, 0, 0]])
point_h = np.hstack((point, np.ones((point.shape[0], 1))))

# Z축 90도 회전
theta = np.deg2rad(90)

Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta),  np.cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# 이동
T_translate = np.array([
    [1, 0, 0, 5],
    [0, 1, 0, 0],
    [0, 0, 1, 2],
    [0, 0, 0, 1]
])

# 회전 후 이동
T_correct = T_translate @ Rz
result_correct = point_h @ T_correct.T

# 이동 후 회전 (순서 반대)
T_wrong = Rz @ T_translate
result_wrong = point_h @ T_wrong.T

print("회전 후 이동 결과:")
print(result_correct[:, :3])

print("\n이동 후 회전 결과:")
print(result_wrong[:, :3])