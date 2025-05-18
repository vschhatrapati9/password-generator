import string  # For letters, digits, and punctuation
import secrets  # For secure random choice


# Check if password contains uppercase letters
def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


# Check if password contains symbols (special characters)
def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


# Function to generate a random secure password
def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    new_password = ''
    for _ in range(length):
        new_password += secrets.choice(combination)


    return new_password


# Main program
if __name__ == '__main__':
    for i in range(5):
        new_pass = generate_password(length=10, symbols=True, uppercase=False)
        specs = f"U:{contains_upper(new_pass)} S:{contains_symbols(new_pass)}"
        print(f"{i + 1}: {new_pass} [{specs}]")
