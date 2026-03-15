# 이스케이프 문자: \와 조합
# \": 큰따옴표 의미
# \': 작은따옴표 의미

print("\"안녕하세요\"라고 말했습니다")
# \n: 줄바꿈
print("안녕하세요\n안녕하세요")
# \t: 탭
print("안녕하세요\t안녕하세요")
# \\: 역슬래시(\)

# string indexing & slicing
print("안녕하세요"[0])        
print("안녕하세요"[-4])     
print("안녕하세요"[1:4])            

s = "안녕하세요"
print(s[1:4])
print(s[1:-2]) # 녕하
print(s[-1]) # 요 (뒤에서 1번째)
print(s[-4]) # 녕
print(s[:-3]) # 안녕 (뒤에서 3번째 글자 전까지)
print(s[-3:]) # 하세요 (뒤에서 3번째부터 끝까지)
print(s[::-1]) # 요세하녕안 (뒤집기)
print(s[::2]) # 안하요 (2칸씩 앞으로 이동)

# type & operators
print(type(52.3))
print(3 // 2)

# string formatting
string_a = "{}".format(10)
output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:+015f}".format(52.345)
output_d = "{:15.3f}".format(52.2345)

print(string_a, output_a, output_b, output_c, output_d)

# strip
x = """
    안녕하세요
"""
print(x.strip())
print(x.lstrip())

# string methods
print("TrainA10".isalnum())
print("안녕안녕하세요".find("안녕"))
print("10 20 30 40".split(" "))
print("::".join(["1", "2", "3", "4", "5"]))

string = input("입력> ")
print("입력 + 100", string+100)
              
int_a = int(string)              
print("입력 + 100", int+100)
print("입력 + 100", int_a+100)

string_a = "{}".format(10)
print(string_a)
print(type(string_a))

# {값:출력형식}
# d: 정수(decimal integer)
print(output_a = "{:d}".format(52))
              
output_a = "{:d}".format(52)
              
print(output_a)

# 총 자릿수 5칸 안에서 뒤에서부터 채움             
output_b = "{:5d}".format(52)   # f"{52:5d}" 와 같은 의미      
print(output_b)

output_c = "{:+d}".format(52)           
print(output_c)

output_a = "{:f}".format(52.432)           
print(output_a)

output_b = "{:15f}".format(52.345)             
print(output_b)

# 공백을 0으로 채움
output_c = "{:015f}".format(52.345)              
print(output_b)

output_c = "{:+015f}".format(52.345)             
print(output_c)
              
output_d = "{:15.3f}".format(52.2345)            
print(output_d)
              
output_a = 52.0    
output_b = "{:g}".format(output_a)
              
print(output_b)

x = """
    안녕하세요
    """
              
print(x)  
print(x.strip())          
print(x.lstrip())
             
print("TrainA10".isalnum())
           
a = "안녕안녕하세요".find("안녕")
              
print(a)
              
a = "10 20 30 40".split(" ")
              
print(a)
              
['10', '20', '30', '40']
import datetime
now = datetime.datetime.now()
print(now.year, "년")
print(now.second, "초")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year, now.month, now.day, now.hour, now.minute, now.second
    ))

import datetime
now = datetime.datetime.now()

if now.hour<12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))

    
if now.hour>=12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))



s = "안녕하세요"
print(s[1:4])
print(s[1:-2])