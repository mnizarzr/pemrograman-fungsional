import math


def translate(tx, ty):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            new_x = x + tx
            new_y = y + ty
            return func((new_x, new_y), m)

        return wrapper

    return decorator


def scale(sx, sy):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            new_x = x * sx
            new_y = y * sy
            return func((new_x, new_y), m)

        return wrapper

    return decorator


def rotate(angle):
    def decorator(func):
        def wrapper(*args):
            (x, y), m = args
            t = math.radians(angle)
            new_x = x * math.cos(t) - y * math.sin(t)
            new_y = x * math.sin(t) + y * math.cos(t)
            return func((new_x, new_y), m)

        return wrapper

    return decorator


y_intercept = lambda p, m: p[1] - m * p[0]


if __name__ == "__main__":
    # Cek kesesuaian dengan modul:
    # x, y = 3, 4
    # m = 2
    # tx, ty = 2, -3
    # angle = 60
    # sx, sy = 1.5, 2

    x, y = tuple(map(int, input("Masukkan titik A (x, y): ").split(",")))
    m = int(input("Masukkan gradien (m): "))
    tx, ty = tuple(
        map(int, input("Masukkan pergeseran translasi (tx, ty): ").split(","))
    )
    angle = float(input("Masukkan sudut rotasi (angle): "))
    sx, sy = tuple(map(float, input("Masukkan faktor skala (sx, sy): ").split(",")))

    point = (x, y)

    def line_equation_of(point, m):
        c = y_intercept(point, m)
        return f"y = {m:.2f}x + {c:.2f}"

    @translate(tx, ty)
    @rotate(angle)
    @scale(sx, sy)
    def eq_after_transformation(point, m):
        c = y_intercept(point, m)
        return f"y = {m:.2f}x + {c:.2f}"

    print(f"Persamaan garis yang melalui titik {point} dan bergradien {m}:")
    print(line_equation_of(point, m))

    print(f"Persamaan garis baru setelah ditransformasi:")
    print(eq_after_transformation(point, m))
