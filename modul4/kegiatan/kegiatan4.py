import math

def translate(tx, ty):
    def inner(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return inner

def dilatasi(sx, sy):
    def inner(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return inner

def rotate(angle):
    def inner(x, y):
        arad = math.radians(angle)
        new_x = x * math.cos(arad) - y * math.sin(arad)
        new_y = x * math.sin(arad) + y * math.cos(arad)
        return new_x, new_y
    return inner

titik_awal = (3, 5)

# Translation
translasi_func = translate(2, -1)
titik_setelah_translasi = translasi_func(*titik_awal)
print("Setelah Translasi:", titik_setelah_translasi)

# Dilatation
dilatasi_func = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_func(*titik_awal)
print("Setelah Dilatasi:", titik_setelah_dilatasi)

# Rotation
rotasi_func = rotate(30)
titik_setelah_rotasi = rotasi_func(*titik_awal)
print("Setelah Rotasi:", titik_setelah_rotasi)
