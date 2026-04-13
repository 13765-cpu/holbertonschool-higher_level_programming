#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # {:d} vasitəsilə yoxlayırıq: əgər integer-dirsə çap edirik
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər element integer deyilsə, səssizcə keçirik (skip)
            continue
        except IndexError:
            # Əgər x siyahının uzunluğundan böyükdürsə, dövrü dayandırırıq
            break
    print("")  # Sonda yeni sətir
    return count
