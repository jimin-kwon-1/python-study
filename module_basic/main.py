import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius)) 


import test_module
print("main __name__:", __name__)
print("test_module __name__:", test_module.__name__)

