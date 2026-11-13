
import secrets
import string
import hashlib

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def hash_password(password):
    result = hashlib.sha256(password.encode())
    return result.hexdigest()


print("1. Generate Password")
print("2. SHA-256 Hash")

choice = input("Choose an option: ")

if choice == "1":

    length = int(input("Enter password length: "))
    count = int(input("How many passwords: "))

    for i in range(count):
        print("Password:", generate_password(length))

elif choice == "2":

    text = input("Enter text: ")

    print("SHA-256:", hash_password(text))

else:
    print("Invalid choice")
