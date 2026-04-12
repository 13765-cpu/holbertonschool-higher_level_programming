#!/usr/bin/python3
"""Square klassını təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size):
        """Kvadratı müəyyən bir ölçü ilə yaradır.

        Args:
            size (int): Kvadratın tərəfinin 
        """
        self.__size = size
