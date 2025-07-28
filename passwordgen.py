
# Password Generator

import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Characters to include in the password
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User input
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
