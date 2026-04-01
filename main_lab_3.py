from labo_3 import *

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
                    continue

                if figure_name in classes_map:
                    try:
                        figure_obj = classes_map[figure_name](*params)
                        figures_list.append((figure_name, figure_obj))
                    except Exception:
                        pass
    except FileNotFoundError:
        return None

    if not figures_list:
        return None

    return max(figures_list, key=lambda item: item[1].volume())

if __name__ == "__main__":
    result = find_largest_figure("input02.txt")
    if result:
        print(f"Найбільша фігура: {result[0]}, її міра: {result[1].volume():.2f}")
    else:
        print("Фігури не знайдено.")