import numpy as np
"""
17_relative_vs_global_angle.py

상대각(theta2)이 왜 theta1+theta2가 되는지 
행렬 체인으로 확인하기
"""
L1 = 2
L2 = 1

theta1 = np.deg2rad(30)
theta2 = np.deg2rad(20)

# -------- 수식 방식 --------
x_formula = L1*np.cos(theta1) + L2*np.cos(theta1 + theta2) # 공식으로 계산한 2링크 로봇팔 끝점의 x좌표
y_formula = L1*np.sin(theta1) + L2*np.sin(theta1 + theta2) # 공식으로 계산한 2링크 로봇팔 끝점의 y좌표

# -------- 행렬 방식 --------
def T(theta, L):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([
        [c, -s, L*c],
        [s,  c, L*s],
        [0, 0, 1]
    ])

T1 = T(theta1, L1)
T2 = T(theta2, L2)

T_total = T1 @ T2 # 엔드이펙터 좌표 → 베이스(월드) 좌표

end = np.array([[0, 0, 1]])
position = end @ T_total.T

print("Formula:", x_formula, y_formula)
print("Matrix:", position[:, :2])