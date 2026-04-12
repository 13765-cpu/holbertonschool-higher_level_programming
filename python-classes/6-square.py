#!/usr/bin/python3
"""Square klassını təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni kvadrat yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçünü əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Mövqeyi əldə etmək üçün getter."""
        return self.__position

    @size.setter
    def position(self, value):
        """Mövqeyi təyin etmək üçün setter."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini hesablayır."""
        return self.__size * self.__size

    def my_print(self):
        """Kvadratı '#' simvolu və mövqe boşluqları ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan buraxılan boş sətirlər (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Kvadratın sətirlərini çap etmək
        for _ in range(self.__size):
            # Soldan buraxılan boşluqlar (position[0]) + kvadratın özü
            print(" " * self.__position[0] + "#" * self.__size)
