#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Bütün arqumentlərin cəmini saxlamaq üçün bir dəyişən
    total = 0

    # sys.argv[0] skriptin adıdır, ona görə də 1-ci indeksdən başlayırıq
    for arg in sys.argv[1:]:
        total += int(arg)

    print(total)
