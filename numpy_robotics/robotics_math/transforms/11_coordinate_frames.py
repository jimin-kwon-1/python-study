"""
11_coordinate_frames.py

좌표계 변환
Robot frame → World frame
"""
# 월드 좌표 = 전체 공간 기준
# 로봇 좌표 = 로봇 기준
# 센서 좌표 = 센서 기준

import numpy as np

# 1. 로봇 좌표계에서의 점
point_robot = np.array([[1, 0]])    # 로봇 기준으로 (1, 0)

print("Robot frame 점:", point_robot)

# 2. 로봇이 월드 좌표계에서 어디 있나
theta = np.deg2rad(90)  # 로봇이 90도 회전되어 있음
tx, ty = 5, 10  # 로봇 위치 (5, 10)

T_world_robot = np.array([
    [np.cos(theta), -np.sin(theta), tx],
    [np.sin(theta),  np.cos(theta), ty],
    [0,              0,              1]
])

# 3. 점을 homogeneous로
ones = np.ones((point_robot.shape[0], 1))
point_robot_h = np.hstack((point_robot, ones))

# 4. 월드 좌표로 변환
point_world = point_robot_h @ T_world_robot.T
print("World frame 점:", point_world[:, :2])

'''
상황

로봇이:월드 기준으로 (5,10)에 있고 90도 돌아가 있다
로봇 좌표에서 (1,0) → 로봇 기준 “앞으로 1”
근데 로봇이 90도 돌아가 있으니까
월드 기준에서는 “위쪽으로 1”
'''