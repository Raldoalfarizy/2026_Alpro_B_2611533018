# Buat file dengan nama nested_for3_2611533018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Pogram ini menggunakan fungsi input ()

batas_3018 = int(input("Masukkan nilai batas: "))
for i in range(batas_3018+1):
    for j in range(batas_3018+1):
        print(i + j, end=" ")
    print()