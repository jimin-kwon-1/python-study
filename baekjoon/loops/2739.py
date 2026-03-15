# 2739
a = int(input())

for i in range(1, 10):
    print("{} * {} =".format(a, i), a * i)

# 더 깔끔한 답
a = int(input())

for i in range(1, 10):
    print(f"{a} * {i} = {a*i}")
