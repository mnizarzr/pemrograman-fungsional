def point(x, y):
    return x, y

def line_equation_of(p1, M):
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (3,6) dan bergradien 1:")
print(line_equation_of(point(3, 6), 1))


# manual
x1, y1 = (3, 6)
m = 1
c = y1 - m * x1
print(f"y = {m:.2f}x + {c:.2f}")
