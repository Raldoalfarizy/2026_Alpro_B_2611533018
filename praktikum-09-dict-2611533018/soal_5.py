
# Soal 5 - Uang Kas Kelas
n = int(input())
total = {}                              # {nama: total setoran}, urutan = kemunculan pertama
 
for _ in range(n):
    name, amount = input().split()
    total[name] = total.get(name, 0) + int(amount)
 
cash = 0
top_name = ""
top_total = 0
for name, t in total.items():
    print(f"{name}: {t}")
    cash += t
    if t > top_total:                   # '>' (bukan '>=') -> kalau seri, yang lebih dulu menang
        top_name = name
        top_total = t
 
print("Total cash:", cash)
print(f"Top contributor: {top_name} ({top_total})")
 