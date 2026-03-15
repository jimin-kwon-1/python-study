import numpy as np

"""
22_inverse_kinematics_two_solutions.py

2-Link Inverse Kinematics 해 2개 (elbow up / elbow down)

입력: 목표 위치 (x,y), 링크 길이 (L1,L2)
출력: (theta1, theta2) 두 세트
"""

# -----------------------------
# 입력값
# -----------------------------
L1 = 2
L2 = 1

x = 2
y = 1

# -----------------------------
# 도달 가능성 체크 (Workspace)
# -----------------------------
# r = 목표점까지의 거리
r = np.sqrt(x**2 + y**2)

# 도달 가능 조건: |L1-L2| <= r <= (L1+L2)
r_min = abs(L1 - L2)
r_max = L1 + L2

if not (r_min <= r <= r_max):
    raise ValueError("목표점이 workspace 밖이라 도달 불가능")

# -----------------------------
# 1) cos(theta2) 계산 (코사인 법칙)
# -----------------------------
# θ2: L1과 L2 사이 각도
cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)

# 부동소수점 오차로 1.00000002 같은 값이 될 수 있어서 안전하게 클리핑
cos_theta2 = np.clip(cos_theta2, -1.0, 1.0) 
# np.clip(value, min, max): 값을 일정 범위 안으로 강제로 제한하는 함수

# -----------------------------
# 2) theta2 해 2개 만들기
# -----------------------------
theta2_up = np.arccos(cos_theta2) # 0 ~ pi (일반적으로 elbow-up 쪽으로 많이 표현)
theta2_down = -theta2_up          # -pi ~ 0 (대칭 해)

# -----------------------------
# 3) theta1 계산 함수
# -----------------------------
def solve_theta1(theta2):
    """
    theta1 = arctan2(y,x) - arctan2(L2*sinθ2, L1 + L2*cosθ2)

    첫 항: 목표점 방향(α)
    둘째 항: 링크 구조 보정각(β)
    """
    # 목표 방향
    alpha = np.arctan2(y,x) # α: base → 목표점 방향 각도

    # 링크 구조 보정각
    beta = np.arctan2(L2*np.sin(theta2), L1 + L2*np.cos(theta2)) # β: 링크 구조 때문에 생기는 보정각
    # α = θ1 + β
    # θ1 = α − β

    # 첫 관절 각도 θ1
    return alpha - beta

theta1_up = solve_theta1(theta2_up)
theta1_down = solve_theta1(theta2_down)

# -----------------------------
# 출력 (deg)
# -----------------------------
print("[Elbow up]")
print("theta1 (deg):", np.degrees(theta1_up))
print("theta2 (deg):", np.degrees(theta2_down))

# -----------------------------
# (검산) Forward Kinematics로 원래 (x,y) 나오나 확인
# -----------------------------
def forward_kinematics(theta1, theta2):
    x_fk = L1*np.cos(theta1) + L2*np.cos(theta1 + theta2)
    y_fk = L1*np.sin(theta1) + L2*np.sin(theta1 + theta2)
    return x_fk, y_fk

x1, y1 = forward_kinematics(theta1_up, theta2_up)
x2, y2 = forward_kinematics(theta1_down, theta2_down)

print("\n[Check FK]")
print("up     ->", x1, y1)
print("down   ->", x2, y2)
print("target ->", x, y)