# Buat file dengan nama perulangan_for4_2611533018.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Pogram ini menggunakan fungsi input ()

tinggi_3018 = int(input("Masukkan tinggi pola (bilangan genap, misal 10) : "))

if tinggi_3018 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3018 = tinggi_3018
    c_3018 = a_3018
    lebar_3018 = (2 * tinggi_3018) - 2

    for i_3018 in range(1, tinggi_3018 + 1):
        b_3018 = c_3018 + 1

        for j_3018 in range(1, lebar_3018 + 1):

            # baris atas dan bawah
            if i_3018 == 1 or i_3018 == tinggi_3018:
                if j_3018 == 1 or j_3018 == lebar_3018:
                    print("#", end="")
                else:
                    print("=", end= "")

            # baris isi
            else:
                if j_3018 == 1 or j_3018 == lebar_3018:
                    print("|", end="")
                else:
                    if j_3018 == c_3018:
                        print("<", end="")
                    elif j_3018 == b_3018:
                        print(">", end="")
                    elif j_3018 == (lebar_3018 - c_3018):
                        print("<", end="")
                    elif j_3018 == (lebar_3018 - c_3018 + 1):
                        print(">", end= "")
                    elif j_3018 > b_3018 and j_3018 < (lebar_3018 - c_3018):
                        print(".", end="")
                    else :
                        print(" ", end="") 
                        
        print()

        # Logika asli java
        a_3018 -= 2

        if a_3018 <= 0:
            c_3018 = (-a_3018) + 2
        else:
            c_3018 = a_3018