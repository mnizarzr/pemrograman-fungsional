def perkalian(a):
    def dengan(b):
        return a*b
    return dengan

kali_2 = perkalian(2)
hasil_kali_2_dengan = kali_2(5)
print(hasil_kali_2_dengan)

hasil = perkalian(3)(5)
print(hasil)
