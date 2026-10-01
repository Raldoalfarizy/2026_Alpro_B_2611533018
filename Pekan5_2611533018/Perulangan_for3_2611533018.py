# Buat file dengan nama perulangan_for3_2611533018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Pogram ini menggunakan fungsi input ()

ulang_3018 = int(input("Masukkan jumlah perulangan = "))

jumlah_3018 = 0
for i in range(1, ulang_3018 + 1):
    print(i, end = " ")
    jumlah_3018 = jumlah_3018 + i

    if i < ulang_3018:
        print("+", end = " ")
    else:
        print("= ", jumlah_3018, end = " ")
print()
print("Jumlah + ", jumlah_3018)