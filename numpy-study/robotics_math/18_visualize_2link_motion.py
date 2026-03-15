import numpy as np
import matplotlib.pyplot as plt

"""
18_visualize_2link_motion.py

2-Link 로봇팔을 시각적으로 확인하기
각도 변화에 따라 끝점이 어떻게 움직이는지 보기
"""

L1 = 2
L2 = 1

def forward_kinematics(theta1, theta2):
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    return x1, y1, x2, y2

# 테스트 각도
theta1 = np.deg2rad(45)
theta2 = np.deg2rad(60)

# 관절 위치 계산
x1, y1, x2, y2 = forward_kinematics(theta1, theta2)

# 시각화
plt.figure() # 새로운 도화지(그래프 창) 생성

# 첫 번째 링크 그리기: (0,0) → (x1, y1) 선 그리기
plt.plot(       # plt.plot( x좌표들 , y좌표들 ): 선 그리는 함수
    [0, x1],    # x좌표: 베이스(0) → 링크1 끝(x1)
    [0, y1],    # y좌표: 베이스(0) → 링크1 끝(y1)
    marker='o') # 끝점에 동그라미 표시

# 두 번째 링크 그리기: (x1,y1) → (x2,y2) 선 그리기
plt.plot(
    [x1, x2],   # x좌표: 링크1 끝 → 링크2 끝
    [y1, y2],   # y좌표: 링크1 끝 → 링크2 끝
    marker='o')  

# 축 범위 설정
plt.xlim(-3, 3) # x축 범위를 -3 ~ 3으로 고정
plt.ylim(-3, 3) # y축 범위를 -3 ~ 3으로 고정
plt.gca().set_aspect('equal', adjustable='box') 
# plt.gca(): 현재 그래프 축 가져오기 (get current axes)
# set_aspect('equal'): x축과 y축 비율을 동일하게
# adjustable='box': 비율 유지하면서 그래프 영역을 맞추는 옵션

plt.grid() # 격자 표시

# 제목 추가
plt.title("2-Link Robot Arm")
plt.show() # 그래프를 실제로 화면에 표시