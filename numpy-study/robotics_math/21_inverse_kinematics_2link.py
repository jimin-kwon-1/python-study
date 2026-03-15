import numpy as np

"""
21_inverse_kinematics_2link.py

목표 위치 (x,y)가 주어졌을 때
로봇 관절 각도 θ1, θ2 계산

[Inverse Kinematics 개념]

Forward Kinematics:
    관절 각도 (θ1, θ2) → 엔드이펙터 위치 (x, y)

Inverse Kinematics:
    목표 위치 (x, y) → 관절 각도 (θ1, θ2)

즉 우리가 원하는 위치에 로봇팔이 가도록
관절 각도를 계산하는 문제이다.

--------------------------------------------------
1. 로봇팔 구조 (2-link planar robot)

base ---- L1 ---- joint ---- L2 ---- end effector

L1 : 첫 번째 링크 길이
L2 : 두 번째 링크 길이

θ1 : base에서 링크1이 x축과 이루는 각도
θ2 : 링크1과 링크2 사이의 관절 각도

링크2의 실제 방향은
    θ1 + θ2

--------------------------------------------------
2. 목표 위치

목표점: (x, y)

베이스에서 목표점까지 거리:
    r = sqrt(x² + y²)

          end(x,y)
            ●
           / \
        L2/   \ r
         /     \
        ●-------●
    joint L1  base

"""

# 링크 길이
L1 = 2
L2 = 1

# 목표 위치
x = 2
y = 1

# 1. 목표까지 거리
r = np.sqrt(x**2 + y**2)

print("distance", r)

# 2. θ2 계산 (코사인 법칙)
cos_theta2 = (x**2 + y**2 - L1**2 - L2**2)/ (2*L1*L2)

theta2 = np.arccos(cos_theta2) # 코사인 역함수

# 3. θ1 계산
theta1 = np.arctan2(y,x) - np.arctan2(L2*np.sin(theta2),
                                      L1 + L2*np.cos(theta2)) # theta1 = 목표각 - 보정각
# np.arctan2(y, x): 원점 → 목표점(x,y) 방향의 각도

#  결과 출력
print("theta1 (deg):", np.degrees(theta1))
print("theta2 (deg):", np.degrees(theta2))