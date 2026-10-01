# Buat file dengan nama nested_for1_2611533018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Pogram ini menggunakan fungsi input ()

batas_3018 = int(input("masukkan nilai batas: "))
for line_3018 in range(1, batas_3018 + 1):
    for j in range(1, (-1 * line_3018 + batas_3018) + 1):
        print(".", end = " ")
    print(line_3018)