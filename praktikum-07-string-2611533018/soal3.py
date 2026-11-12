# Name: Raldo Restanggi Alfarizy
# NIM: 2611533018
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Algoritma dan Pemrograman"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)

text = "Raldo Restanggi Alfarizy"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)