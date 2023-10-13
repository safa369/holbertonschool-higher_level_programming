#!/usr/bin/python3
"""a model class named Rectangle"""


class Rectangle:
    """a class named Rectangle
    Attribute:
        attr1(width): a width of rectangle of type integer
        attr2(height): a height of rectangle of type integer
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        r = ""
        if self.__height == 0 or self.__width == 0:
            return r
        else:
            for _ in range(self.height):
                r += str(self.print_symbol) * self.width + '\n'
        return r[:-1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ar = self.__height * self.__width
        return ar

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            per = 0
        else:
            per = (self.__width + self.__height) * 2
        return per

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
