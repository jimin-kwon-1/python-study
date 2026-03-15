import numpy as np
"""
23_coordinate_transform.py

좌표계 변환 예제

camera frame → robot frame
"""

# 카메라에서 본 점
p_camera = np.array([[2,1,1]])

# 카메라가 로봇 기준으로 (1,0) 위치
T_robot_camera = np.array([
    [1,0,1],
    [0,1,0],
    [0,0,1]
])

# 좌표 변환
p_robot = p_camera @ T_robot_camera.T

print("camera:", p_camera)
print("robot:", p_robot)