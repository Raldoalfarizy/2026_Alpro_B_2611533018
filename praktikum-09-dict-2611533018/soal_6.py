# Soal 6 (Bonus) - Jadwal Kuliah
schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a - hari terpadat
busiest = ""
most = 0
for day, courses in schedule.items():
    if len(courses) > most:
        busiest = day
        most = len(courses)
print(f"Busiest day: {busiest} ({most} courses)")

# 6b - berapa hari sebuah mata kuliah muncul
course = input()
days = 0
for courses in schedule.values():
    if course in courses:
        days += 1
print(f"{course}: {days} days")