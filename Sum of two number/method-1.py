# Method 1: Brute Force Algorithm
"""
All the possible ways or all the possible solutions to a given problem are enumerated.

"""


def sum_of_two_number(my_list, target):
    for i in range(len(my_list)-1):
        firstNum=my_list[i]
        for j in range(i+1, len(my_list)):
            second_num = my_list[j]
            if (firstNum+second_num==target):
                return [firstNum, second_num]
    return []

my_list= [2,4,7,8]
target = 11
result = sum_of_two_number(my_list, target)

if (result):
    print(result)
else:
    print("There are no elements whose sum is {}".format(target))