import numpy as np

# 로봇의 월드에서 위치/자세
theta = np.deg2rad(90)
tx, ty = 5, 10

T_world_robot = np.array([
    [np.cos(theta), -np.sin(theta), tx],
    [np.sin(theta),  np.cos(theta), ty],
    [0,              0,              1]
])

# 월드 좌표의 점 1개
p_world = np.array([[5, 11]], dtype=float)

# homogeneous로
p_world_h = np.hstack((p_world, np.ones((p_world.shape[0], 1))))


# ✅ 월드→로봇 변환은 역행렬
T_robot_world = np.linalg.inv(T_world_robot)
# inv(T_world_robot): 월드 점을 로봇으로 데려옴

# T_world_robot: robot → world 로 보내는 변환
# T_robot_world: world → robot 로 데려오는 변환
# 서로 반대 방향이므로 역행렬
p_robot = p_world_h @ T_robot_world.T

print("T_world_robot:\n", T_world_robot)
print("\nT_robot_world (inverse):\n", T_robot_world)
print("\nWorld 점:", p_world)
print("Robot 점:", p_robot[:, :2])


# np.linalg.inv: 행렬의 역행렬(inverse matrix) 을 구하는 함수
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

A_inv = np.linalg.inv(A)

print("A:\n", A)
print("\nA_inv:\n", A_inv)
print("\nA @ A_inv:\n", A @ A_inv)
print("\nA_inv @ A:\n", A_inv @ A)
