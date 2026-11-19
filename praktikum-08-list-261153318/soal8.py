number_of_rows = 4
seats_per_row = 5
# write your code below

seats = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]

total_booked = 0

while True:
    
    for i in range(len(seats)):
        row_str = f"Row {i + 1}: " + " ".join(seats[i])
        print(row_str)

    row_input = int(input("Row (0 to stop): "))
    if row_input == 0:
        break

    seat_input = int(input("Seat: "))

    if row_input < 1 or row_input > number_of_rows or seat_input < 1 or seat_input > seats_per_row:
        print("Invalid seat.")
    else:
        r_idx = row_input - 1
        s_idx = seat_input - 1

        if seats[r_idx][s_idx] == "X":
            print("Seat already taken.")
        else:
            seats[r_idx][s_idx] = "X"
            print("Seat booked.")
            total_booked += 1

print(f"Seats taken: {total_booked}")