# escape characters
print("\"안녕하세요\"라고 말했습니다")
print("안녕하세요\n안녕하세요")
print("안녕하세요\t안녕하세요")

# string indexing & slicing
print("안녕하세요"[0])
print("안녕하세요"[-4])
print("안녕하세요"[1:4])

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
