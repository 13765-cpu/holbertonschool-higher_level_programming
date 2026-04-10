#!/usr/bin/python3
def roman_to_int(roman_string):
    # Girişin doğruluğunu yoxla
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Roma rəqəmlərinin xəritəsi
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Mətni sağdan sola gəzirik (daha rahatdır)
    for char in reversed(roman_string):
        value = roman_map.get(char, 0)

        # Əgər cari dəyər əvvəlkindən (sağdakından) kiçikdirsə, çıxırıq
        if value < prev_value:
            total -= value
        else:
            total += value

        # Cari dəyəri növbəti addım üçün yadda saxlayırıq
        prev_value = value

    return total
