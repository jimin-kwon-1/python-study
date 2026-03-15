import numpy as np
import matplotlib.pyplot as plt

"""
20_workspace_2link.py

2-Link 로봇팔의 workspace(도달 가능한 영역) 시각화
theta1, theta2를 여러 값으로 바꿔가며 엔드이펙터 위치를 많이 찍어서 영역을 만든다.
-------------------
workspace = 로봇이 도달할 수 있는 모든 위치 영역

2-Link 로봇팔에서 엔드이펙터 위치는

    x = L1*cos(theta1) + L2*cos(theta1 + theta2)
    y = L1*sin(theta1) + L2*sin(theta1 + theta2)

theta1, theta2의 모든 가능한 조합을 계산하면 
엔드이펙터가 갈 수 있는 모든 점이 만들어지고
그 점들의 집합이 workspace가 된다.

[Workspace 거리 범위]
-------------------
엔드이펙터가 베이스에서 떨어진 거리 r의 범위가 workspace를 결정한다.
    r = sqrt(x^2 + y^2)

최대 거리 (팔이 완전히 펴졌을 때)
    r_max = L1 + L2

최소 거리 (팔이 접혔을 때)
    r_min = |L1 - L2|

그래서 workspace는
    r_min ≤ r ≤ r_max
범위를 가지는 "도넛 모양 영역"이 된다.

[Workspace 계산 방법]
-------------------
1. theta1을 여러 값으로 만든다
2. theta2도 여러 값으로 만든다
3. 모든 각도 조합에서 엔드이펙터 위치 계산
4. 그 점들을 그래프로 찍는다
"""

# 링크 길이
L1 = 2
L2 = 1

# Forward Kinematics 함수
def forward_kinematics(theta1, theta2):
    # 링크1 끝
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)

    # 엔드이펙터
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    return x2, y2 # 엔드이펙터 위치

# 각도 범위 (샘플 개수 늘릴수록 더 촘촘)
theta1_values = np.linspace(0, 2*np.pi, 200) # 0 ~ 360°를 200개로 나눈다
theta2_values = np.linspace(-np.pi, np.pi, 200) # -180° ~ 180°

# 엔드이펙터 좌표 저장 리스트
x_points = []
y_points = []

# 모든 조합에 대해 끝점 위치 계산
for t1 in theta1_values:
    for t2 in theta2_values:
        x, y = forward_kinematics(t1, t2)
        x_points.append(x)
        y_points.append(y)

# workspace 이론 반지름
r_min = abs(L1 - L2) # 절댓값 (absolute value)
r_max = L1 + L2

# 원(이론 경계) 그리기용 데이터
angles = np.linspace(0, 2*np.pi, 400)

outer_x = r_max * np.cos(angles)
outer_y = r_max * np.sin(angles)

inner_x = r_min * np.cos(angles)
inner_y = r_min * np.sin(angles)

# plot
plt.figure()

# 점을 아주 많이 찍어서 workspace 영역 표시
plt.scatter(x_points, y_points, s=1) # s는 점 크기

# 이론 경계 원
plt.plot(outer_x, outer_y)
plt.plot(inner_x, inner_y)

plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.title("2-Link Robot Arm Workspace")

plt.show()