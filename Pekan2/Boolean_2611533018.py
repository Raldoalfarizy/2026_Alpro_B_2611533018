# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit terakhir NIM contoh : a_3018
# Deklarasi variabel dengan tipe data boolean
is_lulus_3018 = True
is_cumlaude_3018 = True

# Mengunakan Boolean
nilai_3018 = 85
batas_lulus_3018 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3018 = nilai_3018 >= batas_lulus_3018 # Hasilnya akan True

print("=== Check kelulusan ===")
print("Nilai : ", nilai_3018)
print("Apakah lulus? : ", status_kelulusan_3018)
if is_lulus_3018 and is_cumlaude_3018:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")
    