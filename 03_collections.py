# 범위:
# list 메서드
# dict 기본
# counter 패턴
# list/dict 중첩

# list methods
a = [1, 2, 3, 4]
a.append(5)
a.insert(1, 10)
a.extend([4, 5, 6])
a.pop(2)
del a[1]
a.remove(5)
a.clear()

# dictionary basics
dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
dictionary["price"] = 5000
del dictionary["ingredient"]

# counter pattern
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)

# nested structure
character = {
    "name": "기사",
    "level": 12,
    "items": {"sword": "불꽃의 검", "armor": "풀플레이트"},
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for sub in character[key]:
            print(sub, character[key][sub])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, item)
    else:
        print(key, character[key])
