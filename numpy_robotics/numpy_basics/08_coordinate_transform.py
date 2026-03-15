"""
좌표 이동 예제
"""

import numpy as np

# 2D 좌표들
points = np.array([[1, 2],
                   [3, 4],
                   [5, 6]]) # points shape = (3,2)

print("원래 좌표:")
print(points)

# 이동 벡터
shift = np.array([10, 100]) # shift shape = (2,)

# 브로드캐스팅으로 이동
new_points = points + shift 
# 각 점에 동일한 이동(translation)을 적용. (x,y) -> (x+10, y+100)

print("\n이동된 좌표:")
print(new_points)

# 1. 카메라 좌표 보정 (픽셀 이동)
# 2. 라이다 포인트클라우드 평행이동
#    센서 기준좌표 -> 로봇 기준좌표로 옮길 때 translation 들어감
# 3. 맵 좌표계 변환
#    월드좌표, 로봇좌표, 센서좌표 간 이동. translation + rotation