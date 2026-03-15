"""
BOJ 4344 - 평균은 넘겠지
분류: 수학 / 평균 / 카운팅
━━━━━━━━━━━━━━━━━━━━━━━━━━
[문제 요약]
- 여러 테스트 케이스가 주어진다.
- 각 케이스에서 학생들의 점수가 주어진다.
- 평균보다 높은 학생이 몇 퍼센트인지 출력한다.

출력 형식
xx.xxx%
━━━━━━━━━━━━━━━━━━━━━━━━━━
[핵심 개념]

1. 평균 계산
avg = sum(scores) / N

2. 평균보다 높은 학생 카운트
if score > avg:
    cnt += 1

3. 비율 계산
percent = cnt / N * 100

4. 소수점 출력
{:.3f}
━━━━━━━━━━━━━━━━━━━━━━━━━━
[패턴 정리]

평균 + 조건 카운팅

1. 평균 구하기
2. 조건 만족 개수 세기
3. 퍼센트 계산
"""

C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))

    N = data[0]
    scores = data[1:]

    avg = sum(scores)/N

    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    percent = cnt / N * 100

    print(f"{percent:.3f}%")