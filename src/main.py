from q1 import swap
from q2 import find_and_replace
from q3 import update_dictionary
from q4 import string_reverse
from q5 import check_divisibility
from q6 import find_first_negative
from q7 import Car

# Online Python - IDE, Editor, Compiler, Interpreter

#Test Scenarios q1
print("Question 1")
print("Test Data 1: Apple, 10")
print("Test Result 1: ", swap( "Apple", 10))
print("Test Data 2: -9, 17")
print("Test Result 2: ", swap(-9,17))
print("--------------------")

#Test Scenario q2
print("--------------------")
print("Question 2")
print("Test Data 1: [1, 2, 3, 4, 2, 2], 2, 5")
print("Test Result 1: ", find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print("Test Data 2: [apple, banana, apple], apple, orange")
print("Test Result 2: ", find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

#Test Scenario q3
print("--------------------")
print("Question 3")
print("Test Data 1: {}, name, Alice")
print("Test Result 2: ", update_dictionary({}, "name", "Alice"))
print("Test Data 2: {age: 25}, age, 26")
print("Test Result 2: ",update_dictionary({"age": 25}, "age", 26))

#Test Scenario Q4
print("--------------------")
print("Question 4")
print("Test Data 1: Hello World")
print("Test Result 1: ", string_reverse("Hello World"))
print("Test Data 2: Python")
print("Test Result 2: ", string_reverse("Python"))


#Test Scenario Q5
print("--------------------")
print("Question 5")
print("Test Data 1: 10, 2")
print("Test Result 1: ", check_divisibility(10, 2))
print("Test Data 2: 7, 3")
print("Test Result 2: ", check_divisibility(7, 3))

#Test Scenario Q6
print("--------------------")
print("Question 6")
print("Test Data 1: [3, 5, -1, 7, -2, 8]")
print("Test Result 1: ", find_first_negative([3, 5, -1, 7, -2, 8]))
print("Test Data 1: [2, 10, 7, 0]")
print("Test Result 2: ", find_first_negative([2, 10, 7, 0]))

#Test Scenario Q7
print("--------------------")
print("Question 7")
print("Test Data: Toyota, Corolla, 2020")
print("Test Result: ", Car("Toyota", "Corolla","2020").describe_car())

