menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    daily_sales = []
    for menu in menus:
        porsi = int(input(f"Day {day}, {menu}: "))
        daily_sales.append(porsi)
    sales.append(daily_sales)

print("Total per day:")
for i in range(len(sales)):
    total_day = 0
    for j in range(len(sales[i])):
        total_day += sales[i][j]
    print(f"Day {i + 1}: {total_day}")

menu_totals = []
for j in range(len(menus)):
    total_menu = 0
    for i in range(len(sales)):
        total_menu += sales[i][j]
    menu_totals.append((menus[j], total_menu))

print(f"Total per menu: {menu_totals}")

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")