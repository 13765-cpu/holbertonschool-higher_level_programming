#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    # add funksiyası üçün
    print("{} + {} = {}".format(a, b, add(a, b)))

    # sub funksiyası üçün
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # mul funksiyası üçün
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # div funksiyası üçün
    print("{} / {} = {}".format(a, b, div(a, b)))
