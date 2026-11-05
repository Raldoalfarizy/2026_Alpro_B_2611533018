total = 0
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    if number == 0:
        continue
    print("Positive number:", number)
    total += number
print("Total:", total)