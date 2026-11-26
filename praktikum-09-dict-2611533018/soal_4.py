# Soal 4 - Pengumpulan Tugas
all_students = input().split()          # baris 1: seluruh kelas (urutan dipertahankan)
submitted = set(input().split())        # baris 2: set otomatis membuang nomor ganda

not_submitted = set(all_students) - submitted    # operasi set: selisih

print("Submitted:", len(submitted), "students")
print("Not submitted:", len(not_submitted), "students")

for num in all_students:               
    if num not in submitted:
        print(num)
