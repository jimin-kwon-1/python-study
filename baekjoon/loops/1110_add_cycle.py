"""
BOJ 1110 - 더하기 사이클

[핵심 개념]
- 자리 분해: //, %
- 새 수 생성: (일의자리 * 10) + (합의 일의자리)
- 사이클 구조: while + 기준값(start) 저장

[실수 포인트]
- start 저장 안 하면 종료 조건 못 만듦
- 합 전체를 붙이면 안 되고 (s % 10)만 사용
- while N != start 로 바로 쓰면 초기 조건 문제 생길 수 있음
"""

N = int(input())

start = N
count = 0

while True:
    count += 1
    s = (N//10) + (N%10)
    N = (N%10)*10  +  (s%10)
    if N == start:
        break
    
print(count)