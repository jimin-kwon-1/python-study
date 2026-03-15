"""
14_transform_3d_basic.py

3D homogeneous 변환 기초
- 3D 점 만들기
- Z축 회전
- 이동

2D: ( x, y ) → ( x, y, 1 )
행렬 크기: 3x3

3D: ( x, y, z ) → ( x, y, z, 1 )
행렬 크기: 4x4

3D 이동 행렬 구조:
[ 1  0  0  tx ]
[ 0  1  0  ty ]
[ 0  0  1  tz ]
[ 0  0  0   1 ]

3D 회전
Z축 회전:
[ cosθ  -sinθ   0  0 ]
[ sinθ   cosθ   0  0 ]
[  0       0    1  0 ]
[  0       0    0  1 ]
"""
# 원래 점: (1, 0, 0)
# z축 90도 회전하면: (0, 1, 0)
# 이동 (5,0,2) 더하면: (5, 1, 2)
import numpy as np

# 1. 3D 점 (로봇 기준)
point = np.array([[1, 0, 0]]) # x, y, z

# 2. homogeneous 확장
point_h = np.hstack((point, np.ones((point.shape[0],1))))

# 3. Z축 90도 회전
theta = np.deg2rad(90)

Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta),  np.cos(theta), 0, 0],
    [0            ,  0            , 1, 0],
    [0            ,  0            , 0, 1]
])

# 4. 이동
tx, ty, tz = 5, 0, 2
T_translate = np.array([
    [1, 0, 0, tx],
    [0, 1, 0, ty],
    [0, 0, 1, tz],
    [0, 0, 0, 1]
])

# 5. 합성 (회전 후 이동)
T_total = T_translate @ Rz

# 6. 변환 적용
point_transformed = point_h @ T_total.T

print("원래 점:", point)
print("변환 후:", point_transformed[:, :3])