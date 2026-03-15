# 엔트리 포인트를 확인하는 모듈 만들기
PI = 3.141592

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * (radius ** 2)

if __name__ == "__main__":
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))
# 현재 파일이 엔트리 포인트인지 확인하고, 엔트리 포인트일 때만 실행