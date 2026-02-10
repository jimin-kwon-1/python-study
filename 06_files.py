# 범위:
# 파일 쓰기/읽기
# 랜덤 데이터 생성

import random

with open("basic.txt", "w") as file:
    file.write("Hello Python Programming!")

with open("basic.txt", "r") as file:
    contents = file.read()

hanguls = list("가나다라마바사아자차카타파하")
with open("info.txt", "w") as file:
    for _ in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file:
    for line in file:
        name, weight, height = line.strip().split(", ")
        bmi = int(weight) / ((int(height)/100) ** 2)
        print(name, bmi)
