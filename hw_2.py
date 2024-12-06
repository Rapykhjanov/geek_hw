class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area не реализован")

    def info(self):
        raise NotImplementedError("Метод info не реализован")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f"Square side length: {self.__side_length}{Figure.unit}, "
              f"area: {self.calculate_area()}{Figure.unit}")


class Rectangle(Figure):
    def __init__(self, width, length):
        super().__init__()
        self.__width = width
        self.__length = length

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        print(
            f'Rectangle length: {self.__length}{Figure.unit}, '
            f'width: {self.__width}{Figure.unit}, '
            f'area: {self.calculate_area()}{Figure.unit} ')


square1 = Square(5)
square2 = Square(7)
rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(5, 8)
rectangle3 = Rectangle(10, 3)

figures = [square1, square2, rectangle1, rectangle2, rectangle3]
for figure in figures:
    figure.info()