password = input("Enter your password: ")

upper = False
lower = False
digit = False
special = False

special_characters = "!@#$%^&*()-+"

if len(password) >= 8:
    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        elif i in special_characters:
            special = True

    if upper and lower and digit and special:
        print("Password is valid!")
    else:
        print("Invalid password! Make sure it has an uppercase, lowercase, digit, and special character.")
else:
    print("Invalid password! It must be at least 8 characters long.")
