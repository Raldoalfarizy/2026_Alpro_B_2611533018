# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Pogram ini menggunakan fungsi input ()

umur_3018 = int(input("Input Umur Anda = "))
sim_3018 = input("Apakah Anda Memiliki SIM (y/t) = ") [0]

if umur_3018 >= 17 and sim_3018 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3018 >= 17 and sim_3018 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3018 < 17 and sim_3018 == 'y':
    print("Anda belum cukup umur punya SIM")

if umur_3018 < 17 and sim_3018 != 'y':
    print("Anda belum cukup umur bawa motor")