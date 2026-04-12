#!/usr/bin/python3
"""Square klassını təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Yeni kvadrat yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Ölçünü (size) əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü (size) təyin etmək üçün setter.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size * self.__size
