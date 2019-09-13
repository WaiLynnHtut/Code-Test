# # import sys
# # print("Python version")
# # print(sys.version)
# # print("Version info.")
# # print(sys.version_info)


# import datetime
# now = datetime.datetime.now()
# print("Current date and time : ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


# from math import pi
# r  = float(input("Input the radius of the circle : "))
# print("The area of the circle with" + str(r) + "is :"
#       + str(pi * r**2))

# value = input("Input some comma seprated numbers : ")
# list = value.split(",")
# tuple = tuple(list)
# print("list: ", list)
# print("Tuple: ", tuple)

# filename = input("Input the filename: ")
# f_extns = filename.split(".")
# print("The extension of the file is ", repr(f_extns[-1]) )

# color_list = ["Red","Green","White","Black"]
# print("%s %s" % (color_list[0],color_list[-1]))

# birth = (23,11,1994)
# print("%i / %i / %i" % birth)

# num = int(input("Inter a integer: "))
# num1 = int("%s" % num)
# num2 = int("%s%s" % (num,num))
# num3 = int("%s%s%s" % (num,num,num))
# print(num1 + num2 + num3)

# import calendar
# y = int(input("Input the year: "))
# m = int(input("Input the month: "))
# print(calendar.month (y,m))

# from datetime import date
# birth_date = date(1994, 11, 23)
# current_date = date.today()
# My_age = current_date - birth_date
# print("I am " + str(My_age) + "years old.")

# def result(x,y,z):
#       sum = x + y + z
#
#       if x == y == z:
#           sum = sum * 3
#       return sum
#
# print(result(2,3,4))
# print(result(2,2,2))

# def new_string(str):
#     if str[:2] == "Is":
#         return str
#     else:
#         len(str) >= 2
#         return "Is" + str
#
# print(new_string("Is"))
# print(new_string("is"))

# def string(str,n):
#     result = ""
#     for i in range(n):
#         result += str
#     return result
#
# print(string('htut',3))

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# def list_count_4 (nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count += 1
#     return count
#
# print(list_count_4([1,4,4,5,6,7,4,4]))

# def substring_copy(str,n):
#     f_str = 2
#
#     if f_str > len(str):
#         f_str = len(str)
#     substr = str[:f_str]
#
#     result = ""
#     for i in range(n):
#         result += substr
#     return result
# print(substring_copy('linn', 3))
# print(substring_copy('a', 2))

# def is_vowel(all_vowels, char):
#     for data in all_vowels:
#         if char == data:
#             print("This is an vowel.")
#             break
#     else:
#         print("This is not.")
#
# is_vowel(['a','e','i','o','u'], input("Inter an one letter: "))

# def data_group(something):
#     for result in something:
#         output = ''
#
#         while(result > 0):
#             output = output + '*'
#             result -= 1
#
#         print(output)
#
# data_group([5,5,3,8])
#
# def concatenate(list):
#     result = ''
#     element = list.reverse()
#     for element in list:
#         result += str(element)
#     print(result)
#
# concatenate(['Wai', 'Linn ', 'Htut '])
#
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
#
# for result in numbers:
#     if result == 237:
#         print(result)
#         break
#     elif (result % 2) == 0:
#         print(result)

# def sum(x,y,z):
#     if x == y or x == z or y == z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum(1,2,3))
# print(sum(2,2,2))

# def sum(x,y):
#     sum = x + y
#     if sum in range(15, 20):
#         sum = 20
#     else:
#         sum = x + y
#     return  sum
# print(sum(12, 12))
# print(sum(12, 6))

# def test_number(x, y):
#     if x == y or abs(x - y) == 5 or (x + y) == 0:
#         return  True
#     return False
#
#print(test_number(7, 2))

# def add_number(a, b):
#     if isinstance(a, int) and isinstance(b, int):
#         #raise TypeError("Inputs must be integers")
#         return a + b
#
# print(add_number(1, 2))

# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print(f"Name: {name}\nAge: {age}\nAddress: {address}")
#
# personal_details()

# x, y = 2, 3
# #result = x * x + 2 * x * y + y * y
# result = (x + y) ** 2
# print(f"({x} + {y}) ^ 2) = {result}")

# amount = 10000
# rate_interest = 10
# year = 1
#
# future_value = amount * ((1 +( 0.01 * rate_interest))
# ** year)
#
# print(round(future_value))

# def cal_percent(pay_money):
#     percent = 0.02
#     limit_price = 300000
#     if pay_money < limit_price:
#         print(int(pay_money * percent))
#     elif pay_money >= limit_price:
#         print(int(limit_price * percent))
#
# cal_percent(int(input("Enter a value: ")))

# amount = int(input("Enter your credit amount: "))
#
# year = int(input("Enter a years: "))
#
# rate_interest = int(input("Enter a rate interest: "))
# future_value = amount * ((1 + (0.1 * rate_interest)) ** year)
#
# print(int(future_value))

# import struct
# print(struct.calcsize("P") * 8)

# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())
#
# import os
# print("Current File Name : ",os.path.realpath(__file__))
#
# import multiprocessing
# print(multiprocessing.cpu_count())
#
# import getpass
# print(getpass.getuser())

# def remove_num(given_list):
#     positon = 2 - 1
#     index = 0
#     get_list = len(given_list)
#     while get_list > 0:
#         index = (positon + index) % get_list
#         print(given_list.pop(index))
#         get_list -= 1
#
# remove_num([1,2,3,4,4,1,2,1,2])

# numbers = []
# for num in range(10):
#   num=str(num).zfill(3)
# print(num)
# #numbers.append(num)
# print(numbers)

def letter_combination(digit):
  if digit == "":
    return  []
  string_maps = {
      "1": "abc",
      "2": "def",
      "3": "ghi",
      "4": "jkl",
      "5": "mno",
      "6": "pqrs",
      "7": "tuv",
      "8": "wxy",
      "9": "z"
    }

  result =[""]
  for num in digit:
    temp = []
    for an in result:
      for char in string_maps[num]:
        temp.append(an + char)
        result = temp
  return result


print( letter_combination("47"))