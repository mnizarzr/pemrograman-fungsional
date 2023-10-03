def hitung_nilai_akhir(v):
    c = len(v)
    sm = 0
    for i in v.values():
        sm += i
    return sm / c

def hitung_nilai_akhir_semua(data_mahasiswa):
    result = {}
    for k, v in data_mahasiswa.items():
        result[k] = hitung_nilai_akhir(v)
    return result

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "nzr": {
            "uts": 90,
            "uas": 81,
            "tugas": 90
        },
        "zlm": {
            "uts": 90,
            "uas": 90
        }
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)


main()
