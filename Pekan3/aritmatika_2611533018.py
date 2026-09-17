# Buat file dengan nama aritmatika_2611533018.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_3018
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3018 = int(input("Masukkan angka-1: "))
angka2_3018 = int(input("Masukkan angka-2: "))

# Penjumlahan
hasil_penjumlahan_3018 = angka1_3018 + angka2_3018
print("\nOperator Penjumlahan")
print("Hasil =", hasil_penjumlahan_3018)

# Pengurangan
hasil_pengurangan_3018 = angka1_3018 - angka2_3018
print("\nOperator Pengurangan")
print("Hasil =", hasil_pengurangan_3018)

# Perkalian
hasil_perkalian_3018 = angka1_3018 * angka2_3018
print("\nOperator Perkalian")
print("Hasil =", hasil_perkalian_3018)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3018 != 0:
    hasil_pembagian_3018 = angka1_3018 / angka2_3018
    print("\nOperator Pembagian")
    print("Hasil =", hasil_pembagian_3018)

    hasil_pembagian_bulat_3018 = angka1_3018 // angka2_3018
    print("\nOperator Pembagian bulat")
    print("Hasil =", hasil_pembagian_bulat_3018)

    hasil_sisa_bagi_3018 = angka1_3018 % angka2_3018
    print("\nOperator sisa bagi")
    print("Hasil =", hasil_sisa_bagi_3018)
else:
    print("Angka kedua tidak boleh bernilai nol")

# Pangkat
hasil_pangkat_3018 = angka1_3018 ** angka2_3018
print("\nOperator Pangkat")
print("Hasil =", hasil_pangkat_3018)