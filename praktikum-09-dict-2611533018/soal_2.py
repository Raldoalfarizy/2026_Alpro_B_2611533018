# Soal 2 - Dua Grup WhatsApp
class_group = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
batch_group = {"Citra", "Dewi", "Eka", "Fajar", "Gita", "Hana"}

print(class_group & batch_group)         # 2a
print(class_group - batch_group)         # 2b
print(len(class_group | batch_group))    # 2c
print(class_group ^ batch_group)         # 2d
print("Fajar" in class_group)            # 2e

new_group = set()
new_group.add("Andi")
print(new_group)