# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan  identitas
 
print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")
 
# Input beberapa data yang dipisahkan dengan koma
input_data_3018 = input("Masukkan beberapa angka, pisahkan dengan koma: ")
 
# Mengubah input menjadi list integer
data_3018 = [int(angka.strip()) for angka in input_data_3018.split(",")]
 
nilai_dicari_3018 = int(input("Masukkan angka yang ingin dicari: "))
 
# Operator in
hasil_3018 = nilai_dicari_3018 in data_3018
print("\nOperator keanggotaan IN")
print(nilai_dicari_3018, "in", data_3018, "=", hasil_3018)
 
# Operator not in
hasil_3018 = nilai_dicari_3018 not in data_3018
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3018, "not in", data_3018, "=", hasil_3018)