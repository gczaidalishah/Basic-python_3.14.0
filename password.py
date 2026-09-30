import re

password = input("Enter your password: ")

strength = 0

# Length check
if len(password) >= 8:
    strength += 1

# Uppercase letter
if re.search("[A-Z]", password):
    strength += 1

# Lowercase letter
if re.search("[a-z]", password):
    strength += 1

# Number check
if re.search("[0-9]", password):
    strength += 1

# Special character
if re.search("[@#$%^&*()_+!]", password):
    strength += 1


# Result
if strength == 5:
    print("Strong Password")
elif strength >= 3:
    print("Medium Password")
else:
    print("Weak Password")