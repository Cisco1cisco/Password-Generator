"""
    A simple program to generate passwords
"""

# Importing libraries
import string
import random
# Taking input form the user
Password_name = input("Enter the password's name: ")
password_length = input("Enter how many characters you want to create in the new password: ")
# Input validation
while True:
    try:
        password_length = int(password_length)
        if password_length < 10:
            print("A strong password must contain al least 10 characters")
            password_length = input("Enter how many characters you \
                                    want to create in the new password: ")
        else:
            break
    except ValueError:
        print("Please Enter a postive integer value")
        password_length = input("Enter how many characters you \
                                 want to create in the new password: ")
# Creating the lists
list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

# Shuffling the lists
random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

# Creating the new password
FINAL_PASSWORD = []
for i in range(round(password_length * (30/100))):
    FINAL_PASSWORD.append(list1[i])
    FINAL_PASSWORD.append(list2[i])
for i in range(round(password_length * (20/100))):
    FINAL_PASSWORD.append(list3[i])
    FINAL_PASSWORD.append(list4[i])
FINAL_PASSWORD = "".join(FINAL_PASSWORD)

# Printing the Password
print("The password is ", FINAL_PASSWORD)

# Saving the password to the file
with open("Passwords.txt", "a", encoding="utf-8") as pass_file:
    pass_file.write(Password_name + " : " + FINAL_PASSWORD + "\n")
