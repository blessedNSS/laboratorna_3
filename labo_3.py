import math

class Figura:
    def dimention(self):
        raise NotImplementedError

    def perimetr(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError

    def squareSurface(self):
        raise NotImplementedError

    def squareBase(self):
        raise NotImplementedError

    def height(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError

class Triangle(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return "2D"
    def perimetr(self):
        return (self.a + self.b + self.c)

    def square(self):
        p = (self.a + self.b + self.c) / 2
        val_under_root = p * (p - self.a) * (p - self.b) * (p - self.c)
        if val_under_root <= 0:
            return 0
        return math.sqrt(val_under_root)
    def volume(self):
        return self.square()

class Rectangle(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimention(self):
        return "2D"
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b
    def volume(self):
        return self.square()

class Trapezoid(Figura):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def dimention(self):
        return "2D"
    def perimetr(self):
        return (self.a + self.b + self.c + self.d)

    def square(self):
        if self.a == self.b:
            return self.a * self.c
        diff = abs(self.a - self.b)
        p = (diff + self.c + self.d) / 2
        val_under_root = p * (p - diff) * (p - self.c) * (p - self.d)
        if val_under_root <= 0:
            return 0
        h = (2 / diff) * math.sqrt(val_under_root)
        return ((self.a + self.b) / 2) * h
    def volume(self):
        return self.square()

class Parallelogram(Figura):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self._h = h

    def dimention(self):
        return "2D"
    def perimetr(self):
        return 2*(self.a + self.b)
    def square(self):
        return self.a * self._h
    def volume(self):
        return self.square()

class Circle(Figura):
    def __init__(self, radius):
        self.radius = radius
    def dimention(self):
        return "2D"
    def perimetr(self):
        return 2 * math.pi * self.radius
    def square(self):
        return math.pi * (self.radius ** 2)
    def volume(self):
        return self.square()

class Sphere(Figura):
    def __init__(self, radius):
        self.radius = radius
    def dimention(self):
        return "3D"
    def squareSurface(self):
        return 4 * math.pi * (self.radius ** 2)
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a,a,a)
        self._height = h
    def dimention(self):
        return "3D"
    def height(self):
        return self._height
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        r_in = self.a * math.sqrt(3) / 6
        l = math.sqrt(self._height ** 2 + r_in ** 2)
        return 3 * (0.5 * self.a * l)
    def volume(self):
        return (1/3) * self.squareBase() * self._height

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self._height = h
    def dimention(self):
        return "3D"
    def height(self):
        return self._height
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        l1 = math.sqrt(self._height ** 2 + (self.b / 2) ** 2)
        l2 = math.sqrt(self._height ** 2 + (self.a / 2) ** 2)
        return 2 * (0.5 * self.a * l1) + 2 * (0.5 * self.b * l2)
    def volume(self):
        return (1/3) * self.squareBase() * self._height

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    def dimention(self):
        return "3D"
    def height(self):
        return self.c
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        return 2 * (self.a * self.c + self.b * self.c)
    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, radius, h):
        super().__init__(radius)
        self._height = h
    def dimention(self):
        return "3D"
    def height(self):
        return self._height
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        l = math.sqrt(self.radius ** 2 + self._height ** 2)
        return math.pi * self.radius * l
    def volume(self):
        return (1 / 3) * self.squareBase() * self._height


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._height = h
    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def square(self):
        return None
    def height(self):
        return self._height
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        return super().perimetr() * self._height

    def volume(self):
        return self.squareBase() * self._height

def find_largest_figure(filename):
    classes_map = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapezoid,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Sphere,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped,
        "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }

    figures_list = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue
                figure_name = parts[0]
                try:
                    params = [float(p) for p in parts[1:]]
                except ValueError:
                    print(f"Помилка: невірний формат чисел у рядку '{line.strip()}'")
                    continue
                if figure_name in classes_map:
                    try:
                        figure_obj = classes_map[figure_name](*params)
                        figures_list.append((figure_name, figure_obj))
                    except Exception as e:
                        print(f"Помилка при створенні {figure_name}: {e}")
                else:
                    print(f"Невідома фігура у файлі: {figure_name}")

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

    if not figures_list:
        print("Не вдалося завантажити жодної фігури.")
        return None

    largest_fig_tuple = max(figures_list, key=lambda item: item[1].volume())

    return largest_fig_tuple

filename = "input03.txt"
result = find_largest_figure(filename)

if result:
    name, obj = result
    print("РЕЗУЛЬТАТ:")
    print(f"Найбільша міра у фігури: {name}")
    print(f"Значення міри (площа/об'єм): {obj.volume():.2f}")