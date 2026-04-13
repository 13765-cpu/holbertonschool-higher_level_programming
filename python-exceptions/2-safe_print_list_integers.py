#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # 1. İlk öncə elementin mövcudluğunu və tipini eyni anda yoxlayırıq
            value = my_list[i]
            try:
                print("{:d}".format(value), end="")
                count += 1
            except (ValueError, TypeError):
                # Integer deyilsə səssizcə keçirik
                continue
        except IndexError:
            # Siyahı bitəndə IndexError buraya düşür və dövrü dayandırırıq
            break
            
    print("") # Yeni sətir
    return count
