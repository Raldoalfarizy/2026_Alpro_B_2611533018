# Soal 1 - Voting Ketua Kelas (d = 8)
votes = ["Sari", "Sari", "Bayu", "Rina", "Bayu", "Bayu"]
count = {}    
for name in votes:
    if name in count:
        count[name] = count[name] + 1
    else:
        count[name] = 1
print(count)

winner = ""
most = 0
for name, total in count.items():
    if total > most:
        winner = name
        most = total
print(winner, most)