# Buat file dengan nama logika_2611533018.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_3018
# Program ini menggunakan fungsi input ()
# Program operator logika dalam Python

# Masukkan nilai boolean
# Input tidak peka terhadap huruf besar atau kecil
a1_3018 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3018 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3018)
print("A2 =", a2_3018)

# Konjungsi: bernilai true jika keduanya true
hasil_konjungsi_3018 = a1_3018 and a2_3018
print("\nKonjungsi (AND)")
print("A1 and A2 = ", hasil_konjungsi_3018)

# Disjungsi: bernilai true jika salah satunya true
hasil_disjungsi_3018 = a1_3018 or a2_3018
print("\nDisjungsi (OR)")
print("A1 or A2 = ", hasil_disjungsi_3018)

# Negasi A1: membalik nilai A1
hasil_negasi_A1_3018 = not a1_3018
print("\nNegasi A1 (NOT)")
print("not A1 = ", hasil_negasi_A1_3018)

# Negasi A2: membalik nilai A2
hasil_negasi_A2_3018 = not a2_3018
print("\nNegasi A2 (NOT)")
print("not A2 = ", hasil_negasi_A2_3018)

# XOR: bernilai true jika kedua nilai berbeda
hasil_xor_3018 = a1_3018 != a2_3018
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 = ", hasil_xor_3018)
