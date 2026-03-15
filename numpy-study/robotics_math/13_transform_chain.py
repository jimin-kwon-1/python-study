"""
13_transform_chain.py

Camera → Robot 변환을 만들기
상황:
- 카메라가 로봇 기준 (1, 0)에 붙어있다.
- 회전은 없고, 이동만 있다.

2D에서 이동만 있는 homogeneous 변환 행렬은 항상 다음 구조를 가진다:

[ 1  0  tx ]
[ 0  1  ty ]
[ 0  0   1 ]

왜 이렇게 생겼을까?

점 (x, y, 1)에 이 행렬을 곱하면:
x' = x + tx
y' = y + ty
가 되기 때문이다.

(tx, ty)가 이동량이다.

< 변환 합성 (Composition) >
Camera → Robot  =  T_robot_camera
Robot → World   =  T_world_robot

T_world_camera = T_world_robot @ T_robot_camera
행렬곱은
변환을 순서대로 적용하는 것

"""
import numpy as np

# 1️⃣ Camera → Robot
# 카메라가 로봇 기준 (1,0)에 붙어있다고 가정
tx = 1
ty = 0

T_robot_camera = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

print("T_robot_camera:")
print(T_robot_camera)

# 2️⃣ 카메라 원점 확인
# 카메라 좌표계에서 (0,0)은 카메라 중심
p_camera = np.array([[0,0]])

# homogeneous로 확장 (x, y) → (x, y, 1)
p_camera_h = np.hstack((p_camera, np.ones((p_camera.shape[0], 1))))

print("\np_camera_h:")
print(p_camera_h)

# 3️⃣ Robot 좌표로 변환
T_robot = p_camera_h @ T_robot_camera.T

print("\nRobot 좌표로 변환한 결과:")
print(T_robot[:, :2])


"""
예상 결과

카메라 원점 (0,0)은
로봇 기준 (1,0)이 되어야 한다.

출력:
[[1. 0.]]

"""