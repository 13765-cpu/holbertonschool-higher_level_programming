#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
for idx in range(len(my_list)):
    if list_result[idx]:
        print("{:d} is divisible by 2".format(my_list[idx]))
    else:
        print("{:d} is not divisible by 2".format(my_list[idx]))
