# 범위:


# 리스트

# 딕셔너리

# 딕셔너리 선언 방법
a = dict() 
a = {}

a = {'key1':'value1', 'key2':'value2'} # 초기값으로 지정해 선언
a['key3'] = 'value3' # 별도로 선언하여 값 할당 가능
# 존재하지 않는 키 조회할 경우 에러 발생
# try구문으로 예외 처리
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# for 반복문으로 키/값 조회 가능
# items(): 딕셔너리의 (key, value) 쌍을 한 번에 꺼내주는 메소드
for k,v in a.items():
    print(k,v)

# del로 키 삭제
del a['key1']

# 딕셔너리 모듈
# defaultdict 객체
# 존재하지 않는 키에 자동으로 기본값을 만들어주는 딕셔너리
# 존재하지 않는 키 조회할 경우 에러 메시지 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템 생성
# 예시2_숫자 카운팅
import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a)

a['C'] += 1 # 존재하지 않는 키지만, 디폴트 0을 기준으로 자동으로 생성 후 1 더해 최종으로 1 생성
print(a)

# 예시2_리스트 묶기
d = collections.defaultdict(list)

d['group1'].append(10)
d['group1'].append(20)

print(d)

# Counter 객체

# 아이템에 대한 개수를 계산해 딕셔너리로 리턴
# key에는 아이템 값, value엔 아이템 개수 들어간 딕셔너리 생성
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)

# 가장 빈도 수 높은 요수 추출
print(b.most_common(1)) # (값, 개수) 출력
print(b.most_common(2)) # 2개 추출

# 개수 접근
print(b[1])

# OrderedDict 객체
# 입력된 순서를 기억하는 딕셔너리
collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})

# 타입 선언
# 1. 이름 선언
a = list()
# 2. 기호 선언
type([]) # 리스트
type(()) # 튜플
type({}) # 딕셔너리
type({1}) # 집합

# while 문

# 리스트에 적용할 수 있는 기본 함수

# reversed()

# enumerate()




# 리스트 메소드
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

# enumerate()
# 여러 가지 자료형을 인덱스를 포함한 enumerate 객체로 리턴
a = [1, 2, 3, 2, 45, 2, 5]

for i, v in enumerate(a):
    print(i, v)

# 리스트 컴프리헨션

# [표현식 for 변수 in 반복가능객체]
nums = [i for i in range(5)]

# [표현식 for 변수 in 반복가능객체 if 조건]
nums = [i for i in range(10) if i % 2 == 0]

[n * 2 for n in range(1, 10+1) if n % 2 == 1]

# 문자열 처리
words = ["apple", "banana", "cat"]
lengths = [len(w) for w in words]

# 딕셔너리 컴프리헨션
a = {key: value for key, value in original.items()}