def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_gradient(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)

    M = calculate_gradient(p1, p2)

    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (1, 3) dan (6, 1):")
print(line_equation_of(point(1, 3), point(6, 1)))

# manual
x1, y1 = (1, 3)
x2, y2 = (6, 1)
m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1
print(f"y = {m:.2f}x + {c:.2f}")
