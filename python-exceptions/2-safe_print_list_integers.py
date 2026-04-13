#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Əvvəlcə integer olub-olmadığını format ilə yoxlayırıq
            print("{:d}".format(my_list[i]), end="")
            # Əgər yuxarıdakı sətir xəta vermədisə, deməli çap etdik
            count += 1
        except (ValueError, TypeError):
            # Integer deyilsə, sadəcə növbəti elementə keçirik
            continue
        except IndexError:
            # Əgər siyahı bitdisə, dövrü tamamilə dayandırırıq
            break
    
    # Dövr bitəndə (xəta olsa da, olmasa da) mütləq yeni sətir
    print("")
    return count
