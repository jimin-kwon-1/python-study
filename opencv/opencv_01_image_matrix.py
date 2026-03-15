import cv2
# ==================================================
# OpenCV 01. 이미지는 행렬이다
# ==================================================
# [개념 정리]
# 1. 이미지는 숫자 배열(numpy.ndarray)이다.
# 2. 컬러 이미지는 (height, width, channel) 구조를 가진다.
# 3. OpenCV는 RGB가 아니라 BGR 순서를 사용한다.
# 4. cv2.imread()로 이미지를 읽을 수 있다.
# 5. 이미지 로드 실패 시 None이 반환되므로 반드시 확인해야 한다.
#
# [핵심]
# - img.shape -> (세로, 가로, 채널수)
# - type(img) -> numpy.ndarray
# ==================================================

# 이미지 불러오기
img = cv2.imread("opencv/test.jpg")

# 이미지 크기 확인
print(img.shape)

# 이미지 출력
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(img))