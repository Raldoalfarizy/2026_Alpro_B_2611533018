# Buat file dengan nama assignment_2611533018.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_3018
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3018 = int(input("Masukkan angka-1: "))
angka2_3018 = int(input("Masukkan angka-2: "))

print("\nNilai awal angka1 =", angka1_3018)
print("\nNilai awal angka2 =", angka2_3018)

# Assignment biasa
hasil_biasa_3018 = angka1_3018
print("\nHasil assignment biasa (=)")
print("Hasil =", hasil_biasa_3018)

# Assignment penambahan
hasil_penambahan_3018 = angka1_3018
hasil_penambahan_3018 += angka2_3018
print("\nHasil assignment penambahan (+=)")
print("Hasil =", hasil_penambahan_3018)

# Assignment pengurangan
hasil_pengurangan_3018 = angka1_3018
hasil_pengurangan_3018 -= angka2_3018
print("\nHasil assignment pengurangan (-=)")
print("Hasil =", hasil_pengurangan_3018)

# Assignment perkalian
hasil_perkalian_3018 = angka1_3018
hasil_perkalian_3018 *= angka2_3018
print("\nHasil assignment perkalian (*=)")
print("Hasil =", hasil_perkalian_3018)

# Assignment pembagian, bilangan bulat, dan sisa bagi
if angka2_3018 != 0:
    hasil_pembagian_3018 = angka1_3018
    hasil_pembagian_3018 /= angka2_3018
    print("\nHasil assignment pembagian (/=)")
    print("Hasil =", hasil_pembagian_3018)

    hasil_pembagian_bulat_3018 = angka1_3018
    hasil_pembagian_bulat_3018 //= angka2_3018
    print("\nHasil assignment pembagian bulat (//=)")
    print("Hasil =", hasil_pembagian_bulat_3018)

    hasil_sisa_bagi_3018 = angka1_3018
    hasil_sisa_bagi_3018 %= angka2_3018
    print("\nHasil assignment sisa bagi (%=)")
    print("Hasil =", hasil_sisa_bagi_3018)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment pemangkatan
hasil_pangkat_3018 = angka1_3018
hasil_pangkat_3018 **= angka2_3018
print("\nHasil assignment pemangkatan(**=)")
print("Hasil =", hasil_pangkat_3018)