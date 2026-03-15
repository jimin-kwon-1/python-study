# 조건문으로 예외 처리하기
user_input_a = input("정수 입력> ")
if user_input_a.isdigit():
    number_input_a = int(user_input_a) # 문자열을 숫자로 변환
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

# try ~ except 문으로 예외 처리하기
# try:
#     예외가 발생할 가능성이 있는 코드
# except:
#     예외가 발생했을 때 처리하는 코드
try:
    number_input_a = int(input("정수 입력> ")) # 예외가 발생할 가능성이 있는 코드
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

# pass 키워드: 예외 처리 코드를 나중에 작성할 때 사용
# 숫자로 변환되는 것들만 리스트에 넣기
list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item) # 예외 발생 시 자동으로 넘어감
        list_number.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는 {}".format(list_input_a, list_number))

# try ~ except ~ else 문
# try:
#     예외가 발생할 가능성이 있는 코드
# except:
#     예외가 발생했을 때 처리하는 코드
# else:
#     예외가 발생하지 않았을 때 처리하는 코드

try:
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# finally 구문: 예외 발생 여부와 상관없이 항상 실행되는 코드
# try:
#     예외가 발생할 가능성이 있는 코드
# except:
#     예외가 발생했을 때 처리하는 코드
# finally:
#     항상 실행되는 코드

try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("코드 실행이 끝났습니다.")

# try + except
# try + except + else
# try + except + finally
# try + except + else + finally
# try + finally

try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print(file.closed)

# try 구문에서 return 이나 break 키워드로 탈출해도 finally 구문은 무조건 실행된다.

# 확인 문제 1
numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("- 리스트 내부에 없는 값입니다.")
print()

# 06-2 예외 고급
# try:
#     예외가 발생할 가능성이 있는 코드
# except 예외의 종류 as 예외 객체를 활용할 변수 이름:
#     예외가 발생했을 때 처리하는 코드

# 예외 객체
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as e:
    print("type(e):", type(e))
    print("e:", e)

# 여러 종류의 예외 처리하기
list_number = [52, 273, 32, 103, 90, 10, 275]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as e:
    print("type(e):", type(e))
    print("e:", e)

# 예외 구분하기
list_number = [52, 273, 32, 103, 90, 10, 275]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해주세요.")
except IndexError:
    print("리스트의 인덱스를 벗어났습니다.")

# Exception 클래스: 모든 예외의 부모 클래스

# raise 키워드: 예외 강제 발생
# raise 예외 객체