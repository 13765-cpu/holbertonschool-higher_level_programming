#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            # 1. Elementlərin mövcudluğunu yoxlayırıq
            # my_list_1[i] və ya my_list_2[i] yoxdursa IndexError verəcək
            val1 = my_list_1[i]
            val2 = my_list_2[i]

            # 2. Bölməni yoxlayırıq
            result = val1 / val2

        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            # Nəticəni (uğurlu bölmə və ya 0) yeni siyahıya əlavə edirik
            new_list.append(result)

    return new_list
