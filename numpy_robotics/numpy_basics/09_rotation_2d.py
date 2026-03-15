"""
09_rotation_2d.py
2D 회전 (Rotation)

핵심:
- 회전행렬 R 만들기
- 점(points)에 회전 적용하기
"""
# 회전
# 2D에서 점 (x, y)를 원점 기준으로 θ만큼 회전시킨 새로운 점 (x', y')
# 𝑥′ = 𝑥cos𝜃 − 𝑦sin⁡𝜃
# 𝑦′ = 𝑥sin𝜃 + 𝑦cos𝜃

# 회전 공식 -> 회전행렬 R
# R = [cos𝜃  -sin𝜃]
#     [sin𝜃   cos𝜃] 

import numpy as np

# 1) 2D 점들 (N개, 각 점은 [x, y])
points = np.array([
    [1, 0],
    [0, 1],
    [1, 1],
    [2, 1]
], dtype=float) # 각 점을 한 행에 저장. 행으로 쌓음

print("원래 점들:\n,", points)

# 2) 회전 각도 (도 -> 라디안)
theta_deg = 90
theta = np.deg2rad(theta_deg) # 90도를 라디안으로 변경

# 3) 2D 회전행렬
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

print(f"\n회전행렬 R ({theta_deg}도):\n", R)

# 4) 회전 적용
# points는 shape: (N,2), R은 (2,2)
# (N,2) @ (2,2) = (N,2)
"""
수학은 열벡터, NumPy는 행벡터 씀
행렬곱: ( m x n ) @ ( n x p )

열벡터 점 하나 v: (2,1)
수학식: R @ v
행렬 전치 규칙: (AB)^T = B^T A^T
(R @ v)^T = v^T @ R^T <= v^T: 행벡터

열벡터 방식 = R @ v
행벡터 방식 = v @ R^T

열벡터는 왼쪽에서 곱한다
행벡터는 오른쪽에서 곱한다
"""
rotated = points @ R

print("\n회전된 점들:\n", rotated)


# practice
import numpy as np

theta = np.deg2rad(90)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v_col = np.array([[1],
                  [0]])  # 열벡터 (2,1)

v_row = np.array([1, 0]) # 행벡터 (2,)

print("열벡터 방식:\n", R @ v_col)
print("행벡터 방식:\n", v_row @ R.T)


# 행벡터 vs 열벡터 비교
import numpy as np

T = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
])

p_col = np.array([[0],
                  [0],
                  [1]])  # 열벡터

p_row = np.array([[0, 0, 1]])  # 행벡터

print("열벡터 방식:")
print(T @ p_col)

print("\n행벡터 방식:")
print(p_row @ T.T)