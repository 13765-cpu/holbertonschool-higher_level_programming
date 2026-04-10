#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Hər bir elementin 2-yə bölünüb-bölünmədiyini yoxlayan list comprehension
    return [i % 2 == 0 for i in my_list]

# Nümunə siyahı
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

# İstədiyin nəticəni çap edən hissə
for idx in range(len(my_list)):
    if list_result[idx]:
        # Əgər True-dursa (bölünürsə)
        print("{:d} is divisible by 2".format(my_list[idx]), end="")
    else:
        # Əgər False-dursa (bölünmürsə)
        print("{:d} is not divisible by 2".format(my_list[idx]), end="")
