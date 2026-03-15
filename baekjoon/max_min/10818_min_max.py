"""
BOJ 10818 - 최소, 최대
분류: 구현 / 리스트 / 최댓값 & 최솟값
━━━━━━━━━━━━━━━━━━━━━━━━━━
[문제 요약]
- N개의 정수가 주어진다.
- 그 중 최솟값과 최댓값을 출력한다.
━━━━━━━━━━━━━━━━━━━━━━━━━━
[핵심 개념]
1) 리스트 입력 받기
   → list(map(int, input().split()))

2) 최솟값 / 최댓값 탐색

3) 한 번의 순회로 둘 다 구할 수 있음
━━━━━━━━━━━━━━━━━━━━━━━━━━
[헷갈렸던 부분]
- max, min을 변수명으로 사용하면
  → 파이썬 내장함수 덮어씀
━━━━━━━━━━━━━━━━━━━━━━━━━━
[패턴 정리]
"최댓값 + 최솟값 탐색"

- 초기값 설정
- 반복하면서 비교
  → 더 크면 max 갱신
  → 더 작으면 min 갱신

"""

# 정수 개수 입력
N = int(input())

# 정수 리스트 입력
nums = list(map(int, input().split()))

# 첫 값을 기준으로 초기화
max_val = nums[0]
min_val = nums[0]

# 반복하면서 최대/최소 찾기
for num in nums:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

# 결과 출력
print(min_val, max_val)

# 더 간단한 코드
N = int(input())
nums = list(map(int, input().split()))

min_num = min(nums)
max_num = max(nums)

print(min_num, max_num)

# 더 파이썬스럽게 줄인 코드
input()
nums = list(map(int, input().split()))
print(min(nums), max(nums))