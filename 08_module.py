# 07-1 표준 모듈
import math
math.sin(1)
math.cos(1)
math.tan(1)
math.ceil(1.2)
math.floor(1.8)

# round 함수: 반올림 (정수 부분이 짝수일 때는 내림, 홀수일 때는 올림)

# from 모듈 이름 import 가져오고 싶은 변수 또는 함수
from math import * # math 모듈의 모든 변수와 함수 가져오기

# import 모듈 as 사용하고 싶은 식별자
import math as m
print(m.sin(1))

# random 모듈
import random

print(random.random()) # random(): 0.0 <= x < 1.0 사이의 float 리턴
print(random.uniform(10, 20)) # uniform(min, max): min <= x < max 사이의 float 리턴
print(random.randrange(10)) # randranage(max): 0 <= x < max 사이의 int 리턴
print(random.randrange(10, 20)) # randrange(min, max): min <= x < max 사이의 int 리턴
print(random.choice([1, 2, 3, 4, 5])) # choice(리스트): 리스트 내부의 요소 랜덤하게 선택
print(random.shuffle([1, 2, 3, 4, 5])) # shuffle(리스트): 리스트 내부의 요소 랜덤하게 섞기
print(random.sample([1, 2, 3, 4, 5], k=2)) # sample(리스트, k=n): 리스트 내부의 요소 중 n개 랜덤하게 선택하여 리스트로 리턴

# from random import random, randrange, choice

# sys 모듈
import sys
print(sys.argv) # argv: 명령 매개변수
print(sys.getwindowsversion()) # getwindowsversion(): 윈도우 버전 정보 리턴
print(sys.copyright) # copyright: 파이썬 저작권 정보 리턴
print(sys.version) # version: 파이썬 버전 정보 리턴

# datetime 모듈
import datetime

print("# 현재 날짜와 시간 구하기")
now = datetime.datetime.now() # 현재 날짜와 시간 리턴
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
                                            now.month,\
                                            now.day,\
                                            now.hour,\
                                            now.minute,\
                                            now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초") # 문자열, 리스트 등 앞에 * 붙이면 요소 하나하나가 매개변수로 지정됨
print(output_a)
print(output_b)
print(output_c)

# 시간 처리하기
import datetime
now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기") # 특정 시간 이후의 시간 구하기
after = now + datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

print("# datetime.timedelta로 시간 빼기") # 특정 시간 이전의 시간 구하기
before = now - datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1)
print(before.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()

print("# now.replace()로 1년 더하기")
output = now.replace(year=now.year + 1)
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# timedelta() 함수를 사용하면 특정 시간의 이전 또는 이후를 구할 수 있음
# 몇 년 후를 구할 때는 replace() 함수 사용하여 날짜값 교체해야 함

# time 모듈
import time
print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("5초가 지났습니다!")

# urllib 모듈: URL을 다루는 라이브러리
from urllib import request

target = request.urlopen("https://www.google.com") # urlopen("주소"): 해당 주소의 웹 페이지를 여는 함수
output = target.read()

print(output)

# 현재 디렉터리를 읽어들이고 파일인지 디렉터리인지 구분하기
import os
output = os.listdir(".") # listdir("경로"): 해당 경로의 파일과 폴더 목록을 리스트로 리턴
print("os.listdir():", output)
print()

print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path): # isdir("경로"): 해당 경로가 폴더인지 확인하는 함수
        print("[폴더]", path)
    else:
        print("[파일]", path)

# 확인 문제
import os
# 폴더를 읽어들이는 함수
def read_folder(path):
    # 폴더의 요소 읽어들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(item):
            # 폴더라면 계속 읽어들이기
            read_folder(item)
        else:
            # 파일이라면 출력하기
            print("[파일]", item)
# 현재 폴더의 파일/폴더 출력하기
read_folder(".")

# 07-2 외부 모듈
# pip 명령어: 파이썬 외부 모듈 설치하는 도구
# pip install 모듈 이름: 모듈 설치
# pip uninstall 모듈 이름: 모듈 제거 

# Beautifulsoup4: HTML, XML 문서 파싱하는 모듈
# BeautifulSoup 모듈로 날씨 가져오기
from urllib import request
from bs4 import BeautifulSoup
# urlopen() 함수로 웹 페이지 열기
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
# BeautifulSoup() 함수로 웹 페이지 파싱하기
soup = BeautifulSoup(target, "html.parser")
# location 태그 찾기
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그 찾아 출력
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저 기온:", location.select_one("tmn").string)
    print("최고 기온:", location.select_one("tmx").string)
    print()
# 태그를 여러 개 찾을 때는 select() 함수, 하나만 찾을 때는 select_one() 함수 사용

# 라이브러리와 프레임워크
# 라이브러리: 정상적인 제어를 하는 모듈. 개발자가 모듈의 기능을 호출하는 형태의 모듈
from math import sin, cos, tan, floor, ceil
print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(1.5))

# 프레임워크: 역제어의 형태로 동작하는 모듈. 개발자가 작성한 코드를 프레임워크가 호출하는 형태의 모듈
# 제어 역전의 여부로 라이브러리와 프레임워크 구분

# 07-3 모듈 만들기

# __name__=="__main__": 이 파일을 직접 실행할 때만 실행되는 코드 작성할 때 사용. 현재 파일이 엔트리 포인트인지 확인할 때 사용하는 코드
# __name__: 파이썬이 모든 파일에 자동으로 넣어주는 특수 변수. (지금 이 파일이 어떤 방식으로 실행됐는지 알려줌)
# 파일을 직접 실행하면 -> __name__ 변수에 "__main__"이 저장됨
# 파일을 import 당하면 -> __name__ 변수에 파일의 이름이 저장됨

# 모듈 이름을 출력하는 모듈 만들기
import test_module

print("# 메인의 __name__ 출력하기")
print(__name__)
print()

# __name__ 활용하기:  현재 파일이 모듈로 실행되는지, 엔트리 포인트로 실행되는지 확인 가능
# 엔트리 포인트: 프로그램의 시작점이 되는 파일
# 패키지
# 모듈이 모여서 구조를 이루면 패키지 라고 함
# 패키지: 모듈을 디렉터리 단위로 묶은 것 (모듈을 모아놓은 폴더)

# __int__.py 파일: 패키지 로드 시 가장 먼저 실행되는 파일. 초기화/ 모듈 묶기/ import 구조 정리 등에 사용
# __all__ 변수: 패키지에서 from 패키지 이름 import * 구문으로 모듈을 읽어들일 때 가져올 모듈의 목록을 정의하는 변수

# 바이너리 데이터: 컴퓨터가 처리하는 0과 1로 이루어진 데이터. 이미지, 동영상, 음성, 실행 파일 등. 용량 작음
# 텍스트 데이터: 사람이 읽을 수 있는 문자로 이루어진 데이터. 일반 텍스트 파일, 소스 코드 파일, HTML 파일 등. 용량 큼

# 인코딩과 디코딩
# 인코딩: 텍스트 데이터를 바이너리 데이터로 변환하는 과정
# 디코딩: 바이너리 데이터를 텍스트 데이터로 변환하는 과정

# 인터넷의 이미지 저장하기
from urllib import request # 모듈을 읽어들임

# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
output = target.read() # read() 함수로 페이지의 바이너리 데이터 읽기
print(output)
# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb") # 바이너리 형식으로 쓰기
file.write(output) # 파일에 데이터 쓰기
file.close()