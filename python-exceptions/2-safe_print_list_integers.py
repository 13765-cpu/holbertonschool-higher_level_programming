#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # {:d} formatı həm rəqəmi çap edir, həm də tipini yoxlayır
            # my_list[i] isə indeksi yoxlayır
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər element rəqəm deyilsə, səssizcə keçirik
            continue
        except IndexError:
            # Əgər siyahı bitdisə, dövrü dayandırırıq (Traceback-in qarşısını alırıq)
            break
    print("")  # Sonda yeni sətir mütləqdir
    return count
