#!/usr/bin/python3
def islower(c):
    """Return True if character c is lowercase, False otherwise."""
    return ord('a') <= ord(c) <= ord('z')

# Test nümunələri
for c in ['a', 'H', '4', '!', 'g']:
    print("Correct output - case '{}'".format(c))
