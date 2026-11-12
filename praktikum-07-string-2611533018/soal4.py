# Name: Raldo Restanggi Alfarizy
# NIM: 2611533018
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-3:]
print(masked)

phone = "0812345678"
masked = phone[:4] + "*" * 3 + phone[-3:]
print(masked)

phone = "082611533018"
masked = phone[:4] + "*" * 5 + phone[-3:]
print(masked)
