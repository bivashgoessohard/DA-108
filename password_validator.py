# This is a simple password strength finder and validator that checks for minimum length and character variety.
# DA-108 lab, 3rd week assignment

# Initialize an empty list to store previously used passwords
password_history = []

while True:
    password = input("Enter a new password: ")

    length = len(password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    for char in password:
        if char.isupper():
            has_upper = True
            upper_count += 1

        elif char.islower():
            has_lower = True
            lower_count += 1

        elif char.isdigit():
            has_digit = True
            digit_count += 1

        else:
            has_special = True
            special_count += 1


    if password in password_history:
        print("This password has been used before. Please choose a different password.")
        continue

    password_history.append(password)


    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Congratulations! Password is strong.")

    elif length >= 6 and ((has_upper + has_lower + has_digit + has_special) >= 3):
        print("Password is moderate. Try to make it stronger.")

    else:
        print("Password is weak. Try again.")


    print("======Password strength analysis======")
    print(f"Length: {length}")
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
    print(f"Digits: {digit_count}")
    print(f"Special characters: {special_count}")

    print(f"Password history: {password_history}")

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        break

    
