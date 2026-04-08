#!/usr/bin/python3
def islower(c):
    """Return True if character c is lowercase, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')

# Bütün ASCII simvolları 32-126 aralığında yoxlayaq
for i in range(32, 127):
    c = chr(i)
    print(f"{c} is {'lower' if islower(c) else 'upper'}")
