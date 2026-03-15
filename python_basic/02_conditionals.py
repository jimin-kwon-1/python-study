# 범위:
# if / for / while
# range, enumerate, reversed
# 중첩 반복문

import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("오전")
else:
    print("오후")

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print(number)

for number in numbers:
    if number % 2 == 1:
        print(number, "홀수")
    else:
        print(number, "짝수")

list_of_list = [[1,2,3], [4,5,6,7], [8,9]]
for line in list_of_list:
    for item in line:
        print(item)

array = [273, 32, 103, 57, 52]
for i, value in enumerate(array):
    print(i, value)

for i in reversed(range(5)):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1
