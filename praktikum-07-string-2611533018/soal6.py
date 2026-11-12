# Name: Raldo Restanggi Alfarizy
# NIM: 2611533018
# Question 6

#Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

full_name = "  Siti Aisyah  "
nim = "2610511023"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
    
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Muhammad Rafi Pratama"
nim = "2610511045"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
    
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Kartika"
nim = "2610511007"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
    
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Raldo Restanggi Alfarizy"
nim = "2611533018"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
    
username = first_name.lower() + nim[-3:]
print(username)