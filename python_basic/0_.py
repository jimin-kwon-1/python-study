print('A', 'B', sep=',') # sep 파라미터

print('A', end='') # end 파라미터
print('B') # 줄바꿈 안 됨

# 리스트 출력할 때는 join()으로 묶어서 처리
a = ['A', 'B']
print(' '.join(a))

idx = 1
fruit = "Apple"
# idx 값에 1을 더해서 fruit과 함께 출력
print('{0}: {1}'.format(idx + 1, fruit))
# 인덱스 생략도 가능
print('{}: {}'.format(idx + 1, fruit))

# f-string
print(f'{idx + 1}: {fruit}')