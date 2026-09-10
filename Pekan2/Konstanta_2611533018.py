# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit terakhir NIM contoh : jari_3018

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3018 = float(input("Masukkan nilai jari-jari: "))
luas_3018 = PI * jari_3018 * jari_3018
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3018, luas_3018))