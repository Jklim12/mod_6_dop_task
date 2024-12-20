import math

class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)  # Преобразуем кортеж в список

    def __is_valid_color(self, r, g, b):
        is_valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        is_valid_value = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        return is_valid_types and is_valid_value

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        return list(self.__sides)  # Преобразуем кортеж в список

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides) and self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], length, filled=False):
        super().__init__(color, length, filled=filled)
        self.__radius = length / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2

    def set_sides(self, length):
        self.__radius = length / (2 * math.pi)
        super().__init__(self.get_color(), length, filled=self.filled)  # Обновляем длину


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = len(self) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, *([side_length] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side**3


# Проверка
circle1 = Circle((200, 200, 100), 10)  # (Цвет, длина)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())