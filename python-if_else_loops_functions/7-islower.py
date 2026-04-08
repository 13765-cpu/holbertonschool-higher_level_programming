#!/usr/bin/env python3

def islower(c):
    # 'a' hərfinin ASCII kodu 97, 'z' hərfinin kodu isə 122-dir.
    # ord(c) funksiyası simvolun rəqəm qarşılığını verir.
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
