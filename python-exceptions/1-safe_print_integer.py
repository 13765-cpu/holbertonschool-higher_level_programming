#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # {:d} yalnız integer çap edə bilir
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Əgər value integer deyilsə, bura keçid edir
        return False
