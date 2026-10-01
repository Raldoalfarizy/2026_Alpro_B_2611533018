
tinggi_3018 = int(input("Masukkan Tinggi Segitiga: "))

for i_3018 in range(1, tinggi_3018 + 1):

    for j_3018 in range(tinggi_3018 - i_3018):
        print("", end=" ")

    for j_3018 in range(i_3018):
        print("*", end=" ")

    print()