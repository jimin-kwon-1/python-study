import numpy as np

"""
16_forward_kinematics_2link.py

2-Link 2D Robot Arm Forward Kinematics (정기구학)

목표:
- 링크 길이 L1, L2
- 관절 각도 theta1, theta2
가 주어졌을 때, 엔드이펙터(끝점)의 (x,y) 위치를 구한다.

핵심 아이디어:
- 각 링크는 "회전 + (자기 x축으로) 이동" 이다.
- 이를 2D homogeneous 변환행렬 T로 표현한다.
- 연속된 변환은 행렬곱으로 연결한다: T_total = T1 @ T2

"""
# -------------------------
# 1) 파라미터 설정
# -------------------------
L1 = 2.0
L2 = 1.0

theta1_deg = 90
theta2_deg = 0

# 도(degree) -> 라디안(radian)
theta1 = np.deg2rad(theta1_deg)
theta2 = np.deg2rad(theta2_deg)

# 끝점 좌표 계산
x = L1*np.cos(theta1) + L2*np.cos(theta1 + theta2)
y = L1*np.sin(theta1) + L2*np.sin(theta1 + theta2)

print("End Effector Position:")
print("x =", x)
print("y =", y)


# -------------------------
# 2) 링크 변환행렬 만들기 함수
# -------------------------
def T_rot_trans(theta: float, L: float) -> np.ndarray:
    """
    2D에서 "theta만큼 회전 + 자기 x축으로 L만큼 이동"을 하나의 행렬로 만든다.
    homogeneous 구조:
    [ 회전  |  이동 ]
    [  0 0  |   1  ]

    T =
    [ cos -sin  Lcos ]
    [ sin  cos  Lsin ]
    [  0    0    1   ]
    """
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, -s, L * c],
        [s,  c, L * s],
        [0, 0, 1]
    ], dtype=float)

# -------------------------
# 3) 각 링크 변환행렬
# -------------------------
# 베이스 -> 링크1 끝
T1 = T_rot_trans(theta1, L1)

# 링크1 끝 -> 링크2 끝(엔드이펙터)
T2 = T_rot_trans(theta2, L2)

# -------------------------
# 4) 전체 변환 (체인)
# -------------------------
T_total = T1 @ T2 # 엔드이펙터 좌표 → 베이스(월드) 좌표 변환

# -------------------------
# 5) 엔드이펙터 위치 구하기
# -------------------------
# 엔드이펙터 좌표계에서 원점(끝점)은 (0,0,1)
p_end = np.array([[0, 0, 1]], dtype=float) # 엔드이펙터 좌표계에서의 (0,0)점 (=원점)을 homogeneous로 쓴 것 (마지막 1은 이동)

# 행벡터 방식이므로 p @ T.T

p_world = p_end @ T_total.T 
# p_end: 엔드이펙터 좌표계에서의 한 점(보통 원점) -> homogeneous (x, y, 1)
# # p_world: 월드에서 표현된 같은 점
# T_total: 엔드이펙터 좌표계의 점을 베이스(월드) 좌표로 보내는 2D homogeneous 변환(3x3)
# 점(행벡터) @ 변환행렬.T

print("theta1, theta2 (deg):", theta1_deg, theta2_deg)
print("T1:\n", T1)
print("T2:\n", T2)
print("T_total:\n", T_total)
print("End Effector Position (x,y):", p_world[:, :2])

# -------------------------
# 6) 검산(공식으로도 같은지 확인)
# -------------------------
# 수학 공식:
# x = L1*cos(theta1) + L2*cos(theta1+theta2)
# y = L1*sin(theta1) + L2*sin(theta1+theta2)
x_formula = L1*np.cos(theta1) + L2*np.cos(theta1 + theta2)
y_formula = L1*np.sin(theta1) + L2*np.sin(theta1 + theta2)

print("Formula Position (x,y):", np.array([[x_formula, y_formula]]))



# practice
# 이동만 있는 변환 (x로 10, y로 100 이동)
T = np.array([
    [1, 0, 10],
    [0, 1, 100],
    [0, 0, 1]
], dtype=float)

p = np.array([[0, 0, 1]], dtype=float) # 변환 전 점
print(p @ T.T)  # 결과: [[10, 100, 1]]