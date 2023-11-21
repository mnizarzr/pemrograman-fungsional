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

    # NIM yang digunakan adalah 3 digit terakhir [xyz].
    # Sehingga titik A (x,y); gradien = x; tx = y; ty = z; sx = z; sy = x
    #
    # 3, 6, 1 = x, y, z
    # A (3, 6) | m = 3
    # tx = 6 | ty = 1
    # sx = 1 | sy = 3

    while True:
        nim = str(input("Masukkan 3 digit terakhir NIM: "))

        if len(nim) == 3:
            x, y, z = map(int, nim)
        else:
            print("Harus 3 digit")
            continue

        point = (x, y)
        m = x
        tx, ty = y, z
        sx, sy = z, x

        def line_equation_of(point, m):
            c = y_intercept(point, m)
            return f"y = {m:.2f}x + {c:.2f}"

        @translate(tx, ty)
        @rotate(60)
        @scale(sx, sy)
        def eq_after_transformation(point, m):
            c = y_intercept(point, m)
            return f"y = {m:.2f}x + {c:.2f}"

        print(f"Persamaan garis yang melalui titik {point} dan bergradien {m}:")
        print(line_equation_of(point, m))

        print(
            f"Persamaan garis baru setelah ditransformasi:"
        )
        print(eq_after_transformation(point, m))
