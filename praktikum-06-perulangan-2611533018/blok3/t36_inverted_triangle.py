height = int(input("Enter height: "))
for row in range(height, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()