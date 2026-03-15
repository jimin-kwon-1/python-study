"""
10_homogeneous_transform.py

회전 + 이동을 한 번에 처리하기
"""

import numpy as np

# 1. 원래 점들 (N,2)
points = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
], dtype=float)
# shape = (3,2)

print("원래 점들:")
print(points)

# 2. 90도 회전
theta = np.deg2rad(90)

R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# 3. 이동 벡터
t = np.array([10,100])

# 4. 회전 후 이동 (기존 방식)
Rotated = points @ R.T
transformed = Rotated + t

print("\n회전 후 이동:")
print(transformed)

# 문제점: 2단계 (회전 -> 이동)

# homogeneous 좌표 (동차좌표)
# (x,y)를 (x,y,1)로 확장 -> 행렬곱 한 번으로 회전+이동 동시에

# 5️. homogeneous 변환 행렬 만들기 (3x3)
T = np.array([
    [np.cos(theta), -np.sin(theta), 10],
    [np.sin(theta),  np.cos(theta), 100],
    [0,              0,             1 ]
])

# 6. 점을 homogeneous로 변환
ones = np.ones((points.shape[0], 1)) 

# np.ones(shape): 1로 채워진 배열 만듦 
# np.ones((행개수, 1)) : (x,y) → (x,y,1) 만들기 위해 1이 점 개수(행 개수)만큼 필요
# points.shape[0] = 3 행 개수(점 개수) => ones.shape=(3,1)

points_h = np.hstack((points, ones)) 
# np.hstack((A, B)): 가로로 붙이기 (hstack = horizontal stack)
# points가 (N,2), ones가 (N,1) 이 둘을 가로로 붙여서 (N,3) 만들기 # points_h.shape=(3,3)
"""
points        np.ones
(3,2)          (3,1)

[1, 0],        [ 1 ]
[0, 1],        [ 1 ]
[1, 1]    +    [ 1 ]
      ↓ hstack
points_h
[1, 0, 1 ]
[0, 1, 1 ]
[1, 1, 1 ] 
"""
# 7. 한 번에 변환
result = points_h @ T.T
"""
homogeneous 행렬 T는 열벡터 기준으로 설계되어 있다.
수학적으로는 T @ p_col
NumPy에서는 p_row @ T.T
"""

print("\nHomogeneous 변환 결과:")
print(result[:, :2]) # 모든 행에서 0,1번째 열




# practice
import numpy as np

p = np.array([[1, 0]])  # 점 1개 (1,2)

tx, ty = 10, 100

T = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

p_h = np.hstack((p, np.ones((p.shape[0], 1))))  # (1,3) -> [1,0,1]
out = p_h @ T.T

print("p_h:", p_h)
print("out:", out)
print("2D 결과:", out[:, :2])