import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Класс определяющий обязательные методы, которые должны быть реализованы в дочерних классах"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    """Класс прямоугольник"""

    def __init__(self, width: float, height: float):
        """Прямоугольник с заданными размерами"""
        self.width = width
        self.height = height

    def area(self):
        """Вычисляет площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """Вычисляет периметр прямоугольника"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Возвращает строковое представление прямоугольника"""
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle(Shape):
    """Класс круг"""

    def __init__(self, radius: float):
        """Создает круг с заданным радиусом"""
        self.radius = radius

    def area(self):
        """Вычисляет площадь круга"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Вычисляет длину окружности"""
        return 2 * math.pi * self.radius

    def __str__(self):
        """Возвращает строковое представление круга"""
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """Класс треугольник"""

    def __init__(self, side1: float, side2: float, side3: float):
        """Создает треугольник с заданными сторонами"""
        # Проверяю неравенства треугольника
        sides = sorted([side1, side2, side3])
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Сумма любых двух сторон должна быть больше третьей")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """Вычисляет площадь треугольника по формуле Герона"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        """Вычисляет периметр треугольника"""
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        """Возвращает строковое представление треугольника"""
        return f"Triangle(side1={self.side1}, side2={self.side2}, side3={self.side3})"


def print_shape_info(shape: Shape):
    """Выводит информацию о геометрической фигуре"""

    print(f"Фигура: {shape}")
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print()

# Пример
if __name__ == "__main__":
    shapes = [
        Rectangle(2, 10),
        Circle(6),
        Triangle(4, 4, 6)
    ]

    for shape in shapes:
        print_shape_info(shape)