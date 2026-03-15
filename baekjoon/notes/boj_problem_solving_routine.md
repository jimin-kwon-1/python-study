
# Problem Solving Routine (BOJ) — Final Cheat Sheet

## 0) 10초 체크리스트
1. 입력 구조: T(테스트케이스)? N(개수)? 한 줄/여러 줄?  
2. 출력 구조: 한 번? 여러 줄? 공백/줄바꿈/형식 요구?  
3. 핵심 키워드: 합/개수/최댓값/연속/서로 다른/정렬/사이클/그리디/DP/그래프…  
4. 상태 필요?: “이전 값이 현재에 영향” → 상태 변수(streak, prev, cur 등)  
5. 자료구조 필요?: 중복 제거(set), 빈도(dict/list), 큐/스택, 그래프…

---
## 1) 입력 패턴 빠른 매칭
- `N X` 같이 여러 값 한 줄: `map(int, input().split())`
- 여러 줄 대량 입력: `sys.stdin.readline`
- EOF(끝까지 입력): `try/except` 또는 `for line in sys.stdin`

---
## 2) 유형별 “키워드 → 변수/패턴” 매핑

### A) 합/누적 (total, prefix)
- 키워드: 합, 총합, 누적, 점수, 합계, 전체
- 변수: `total = 0`
- 패턴: `total += x`

### B) 개수/횟수 (cnt)
- 키워드: 몇 개, 횟수, 개수, count
- 변수: `cnt = 0`
- 패턴: `if cond: cnt += 1`

### C) 최댓값/최솟값 + 위치 (max_val/min_val, idx)
- 키워드: 최대, 최소, 가장 큰/작은, 몇 번째, 위치
- 변수: `max_val = -inf`, `max_idx = -1`
- 패턴:
  - `if x > max_val: max_val = x; max_idx = i`

### D) 연속/구간 (streak, best)
- 키워드: 연속, 계속, 끊기면 초기화, OX, 같은 값이 이어짐
- 변수: `streak = 0`, `best = 0`
- 패턴:
  - `if cond: streak += 1; best = max(best, streak)`
  - `else: streak = 0`

### E) 빈도수 카운팅 (freq / dict)
- 키워드: 등장 횟수, 빈도, 0~9 개수, 알파벳 개수
- 선택:
  - 범위 작음(0~9/알파벳 등) → `freq = [0]*K`
  - 값 범위 큼/모름 → `freq = {}` 또는 `collections.Counter`
- 패턴:
  - 리스트: `freq[index] += 1`
  - 딕트: `freq[x] = freq.get(x, 0) + 1`

### F) 필터링/선택 출력 (ans)
- 키워드: ~보다 작은/큰 것만, 조건 만족만, 골라서 출력
- 변수: `ans = []`
- 패턴:
  - `if cond: ans.append(x)`
  - `print(*ans)` (공백 출력)

### G) 사이클/반복해서 원래로 (start, cur, count)
- 키워드: 다시 돌아오면, 사이클 길이, 원래 수로
- 변수: `start = 초기값`, `cur = start`, `count = 0`
- 패턴:
  - `while True: count += 1; cur = next(cur); if cur == start: break`

### H) 유니크/중복 제거/종류 개수 (set)
- 키워드: 서로 다른, distinct, unique, 중복 제거, 종류, 몇 종류
- 변수: `seen = set()`
- 패턴:
  - `seen.add(value)`
  - `print(len(seen))`

### I) 정렬/우선순위 (sort key)
- 키워드: 정렬, 오름차순/내림차순, 기준(key)
- 패턴:
  - `arr.sort()`, `arr.sort(reverse=True)`
  - `arr.sort(key=lambda x: ...)`

### J) 투 포인터/슬라이딩 윈도우 (l, r, window)
- 키워드: 연속 부분, 구간 합, 두 수의 합, 최단/최장 구간
- 변수: `l=0, r=0`, `cur_sum=0`
- 패턴:
  - 조건 맞추며 `l/r` 이동
  - 윈도우 업데이트

### K) 이분 탐색 (lo, hi, mid)
- 키워드: “최솟값/최댓값을 찾아라”, “가능/불가능”, 정렬되어 있음
- 변수: `lo, hi`
- 패턴:
  - `while lo <= hi: mid = (lo+hi)//2`

### L) 그리디 (현재 최선)
- 키워드: 최소 횟수, 최소/최대 만들기, 정렬 후 선택
- 패턴:
  - 정렬 후 규칙대로 선택
  - 증명 느낌: “지금 이 선택이 최적을 망치지 않는다”

### M) DP (dp 배열)
- 키워드: 경우의 수, 최적값, ~까지의 최대/최소, 반복되는 부분문제
- 변수: `dp = [...]`
- 패턴:
  - `dp[i] = dp[i-1] ...` 같은 점화식

### N) 스택 (stack)
- 키워드: 괄호, “이전 것과 짝”, 되돌리기, NGE(오큰수)
- 변수: `stack = []`
- 패턴:
  - push/pop
  - top 확인

### O) 큐/덱 (queue/deque)
- 키워드: FIFO, BFS 준비, 회전, 앞뒤 삽입/삭제
- 변수: `from collections import deque; q=deque()`

### P) BFS/DFS (graph traversal)
- 키워드: 연결, 최단거리(가중치 1), 탐색, 그래프/격자
- 변수:
  - `visited`, `q=deque()`
- 패턴:
  - BFS: 큐
  - DFS: 재귀/스택

### Q) 문자열 파싱/가공
- 키워드: 분리(split), 치환(replace), 접두/접미, 팰린드롬
- 패턴:
  - `split()`, `strip()/rstrip()`
  - 인덱싱/슬라이싱

### R) 수학/정수 자리수
- 키워드: 자리수, 각 자리, 소수, 최대공약수, 나머지
- 패턴:
  - 자리 분해: `n//10`, `n%10`
  - gcd: `math.gcd(a,b)`

---
## 3) 설계 템플릿 (항상 이 순서로)
1. 입력을 그대로 코드로 옮긴다 (형식 확인)
2. 출력 횟수(한 번/여러 번) 결정 → 반복문 위치 확정
3. 규칙에서 **상태 변수** 필요한지 체크 (연속/이전값/누적)
4. 키워드로 유형 매칭(A~R) → 변수 1~3개만 잡기
5. 예제 1개를 손으로 3~5스텝 시뮬레이션
6. 구현 → 제출 → 틀리면 “입력/출력/인덱스/초기값”부터 의심

---
## 4) 빠른 매칭 예시
- 8958(OX퀴즈): D(연속) + A(누적)
- 2577(숫자 개수): E(빈도수 배열)
- 1110(더하기 사이클): G(사이클)
- 10871(X보다 작은 수): F(필터링)
- 3052(나머지): H(set 유니크 개수) + R(나머지)

---
## 5) 출력 실수 방지 체크
- 공백 출력 필요하면 `print(*ans)` 또는 `end=" "`
- print(a, b)는 기본 sep=" "라서 사이 공백 1칸 자동
- 개행은 `\n`, 문자열 입력은 필요시 `.rstrip()`/`.strip()`