#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Siyahıdan kənara çıxanda (IndexError) bura heç bir except-ə girmir
            # Və birbaşa proqramın dayanmasına (Traceback) səbəb olur
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Yalnız tip xətalarını tuturuq (string-ləri keçmək üçün)
            pass
    print("")
    return count
