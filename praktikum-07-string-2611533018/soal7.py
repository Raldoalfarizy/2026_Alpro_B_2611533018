# Name: Raldo Restanggi Alfarizy
# NIM: 2611533018
# Question 7

full_name = "Raldo Restanggi Alfarizy"
nim = "2611533018"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
    
username = first_name.lower() + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10} : {full_name.title()}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {username}")
print(f"{'Intake':<10} : {intake}")
print("=" * 30)