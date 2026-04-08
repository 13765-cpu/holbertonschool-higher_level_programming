#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Simvolun kiçik hərf olub-olmadığını ASCII kodu ilə yoxlayırıq
        # 'a' = 97, 'z' = 122
        if ord(char) >= 97 and ord(char) <= 122:
            # Kiçik hərfi böyük hərfə çevirmək üçün 32 çıxırıq
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    # Bütün hərflər çap olunduqdan sonra yeni sətirə keçid
    print("")
