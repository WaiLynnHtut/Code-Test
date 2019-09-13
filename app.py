# x = 10 + 4 * 4 / 2
# print(x)

# strings_ = [str(x) for x in input("Please input at least 5 words (Use Space): ").split()]
#
# for index,item in enumerate(strings_):
#
#     def recursion_reverse(string_1):
#         if not string_1:
#             return ""
#         else:
#             front_part=recursion_reverse(string_1[1:])
#             back_part=string_1[0]
#
#
#
#         return front_part+back_part[0]
#
#     strings_[index]=recursion_reverse(item)
#
# print(strings_)

def display_data(data):
    for result in data:
        count = ''
        while result > 0:
            count += '*'
            result -= 1
        print(count)
display_data([2,3,4,3])
