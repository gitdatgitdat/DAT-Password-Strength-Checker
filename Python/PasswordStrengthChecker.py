import re

try:
    import pwinput
    use_pwinput = True
except ImportError:
    import getpass
    use_pwinput = False

print("="*30)
print(" Password Strength Checker ")
print("="*30 + "\n")

while True:
    password = pwinput.pwinput(prompt="Enter password to check or type exit to quit: ", mask='*')

    if password.lower() == 'exit':
        print("Goodbye!")
        break

    score = 0

    #Rules
    has_length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search (r'[a-z]', password)
    has_digit = re.search (r'\d', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)

    #Scoring
    if has_length:
        score += 1
        print("Length check passed")
    else:
        print("Password is too short (Minimum 8 characters)")

    if has_upper:
        score += 1
        print("Uppercase letter check passed")
    else:
        print("No uppercase letters found")

    if has_lower:
        score += 1
        print("Lowercase letter check passed")
    else:
        print("No lowercase letters found")

    if has_digit:
        score += 1
        print("Number check passed")
    else:
        print("No numbers found")

    if has_special:
        score += 1
        print("Special character check passed")
    else:
        print("No special characters found")

    #Score
    print(f"\nPassword score: {score} out of 5")

    if score == 5:
        print("This is a strong password")
    elif score >= 3:
        print("This is a decent password")
    else:
        print("This is a weak password")

    print("\n" + "="*30 + "\n")
