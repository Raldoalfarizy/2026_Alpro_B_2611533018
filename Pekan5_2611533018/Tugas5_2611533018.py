# Nama   : Raldo Restanggi Alfarizy
# NIM    : 2611533018
# Tugas  : Praktikum Alpro Pekan 5 - Pola Jam Pasir Kristal Palindromik Berbingkai
# Catatan: seluruh variabel berakhiran 4 digit terakhir NIM (3018)
#          dan semua pola dibentuk dengan for bersarang (tanpa perkalian string).

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3018 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Lebar isi bingkai = 4 * N + 5 karakter '='
lebar_3018 = 4 * n_3018 + 5

# Bingkai Atas
print("#", end="")
for garis_3018 in range(lebar_3018):
    print("=", end="")
print("#")

# Fase 1: Jam Pasir Atas (N turun s.d. 1) 
for baris_3018 in range(n_3018, 0, -1):
    print("| ", end="")                                   # pagar kiri + 1 spasi padding

    for spasi_kiri_3018 in range(2 * (n_3018 - baris_3018)):  # spasi penyeimbang kiri
        print(" ", end="")

    for angka_mundur_3018 in range(baris_3018, 0, -1):    # deret mundur: baris ... 1
        print(angka_mundur_3018, end=" ")

    print("<*>", end="")                                   # poros kristal

    for angka_maju_3018 in range(1, baris_3018 + 1):      # deret maju: 1 ... baris
        print(" ", end="")
        print(angka_maju_3018, end="")

    for spasi_kanan_3018 in range(2 * (n_3018 - baris_3018)):  # spasi penyeimbang kanan
        print(" ", end="")

    print(" |", end="")                                   # 1 spasi padding + pagar kanan
    print()

# Fase 2: Poros Titik Pusat 
print("|", end="")
for spasi_kiri_3018 in range(2 * n_3018 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_3018 in range(2 * n_3018 + 1):
    print(" ", end="")
print("|")

# Fase 3: Jam Pasir Bawah (1 naik s.d. N) 
for baris_3018 in range(1, n_3018 + 1):
    print("| ", end="")

    for spasi_kiri_3018 in range(2 * (n_3018 - baris_3018)):
        print(" ", end="")

    for angka_mundur_3018 in range(baris_3018, 0, -1):
        print(angka_mundur_3018, end=" ")

    print("<*>", end="")

    for angka_maju_3018 in range(1, baris_3018 + 1):
        print(" ", end="")
        print(angka_maju_3018, end="")

    for spasi_kanan_3018 in range(2 * (n_3018 - baris_3018)):
        print(" ", end="")

    print(" |", end="")
    print()

# Bingkai Bawah
print("#", end="")
for garis_3018 in range(lebar_3018):
    print("=", end="")
print("#")