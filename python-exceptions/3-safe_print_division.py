#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        # Sıfıra bölmə halında result None olaraq qalır
        pass
    finally:
        # Nə baş verməsindən asılı olmayaraq nəticə burada çap olunur
        print("Inside result: {}".format(result))
    
    return result
