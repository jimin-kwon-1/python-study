import numpy as np
import matplotlib.pyplot as plt
"""
19_end_effector_trajectory.py

2-Link 로봇팔의 엔드이펙터 궤적을 그리기
theta1을 0~360도까지 변화시키면서
끝점이 어떤 경로를 그리는지 확인
"""
# 링크 길이
L1 = 2
L2 = 1

# Forward kinematics 함수
def forward_kinematics(theta1, theta2):
    
    # 링크1 끝점
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    # 링크2 끝점 (엔드이펙터)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    return x2, y2

# 각도 범위 생성

# np.linspace(0, 2*np.pi, 200): 0부터 2π까지를 200등분한 값들을 만듦 (200은 샘플 개수)
theta1_values = np.linspace(0, 2*np.pi, 200)

# theta2는 고정
theta2 = np.deg2rad(30)

# 궤적 저장 리스트
x_traj = []
y_traj = []

# 각도 변화시키면서 위치 계산
for theta1 in theta1_values: # θ1을 0→2π까지 조금씩 바꾸면서 반복 (엔드이펙터 위치 계산)

    x, y = forward_kinematics(theta1, theta2)

    # 궤적 저장 (끝점 위치 기록)
    x_traj.append(x)
    y_traj.append(y)

# 그래프 그리기
plt.figure()

plt.plot(x_traj, y_traj) # x,y 점들을 순서대로 연결해서 선을 그림

plt.gca().set_aspect('equal', adjustable='box') # x축 1칸 = y축 1칸이 되게 만듦
plt.grid()

plt.title("End Effector Trajectory")

plt.show()