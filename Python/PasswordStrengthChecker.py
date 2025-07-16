import re
import os

#Load common passwords from the file one level up.
common_pws_path = os.path.join(os.path.dirname(__file__), '..', 'common-passwords.txt')

try:
    with open(common_pws_path, 'r') as file:
        common_pws = set(p.strip().lower() for p in file)
except FileNotFoundError:
    print("Warning: common-passwords.txt not found. Skipping weak password check.")
    common_pws = set()

#Pull in pwinput if its available, otherwise use getpass.
try:
    import pwinput
    use_pwinput = True
except ImportError:
    import getpass
    use_pwinput = False

def evaluate_pw(password):
    score = 0
    feedback = []

    #Rules
    has_length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search (r'[a-z]', password)
    has_digit = re.search (r'\d', password)
    has_special = re.search(r'[^A-Za-z0-9]', password)

    #Scoring
    if has_length:
        score += 1
        feedback.append("Length check passed.")
    else:
        feedback.append("Password is too short (Minimum 8 characters).")

    if has_upper:
        score += 1
        feedback.append("Uppercase letter check passed.")
    else:
        feedback.append("No uppercase letters found.")

    if has_lower:
        score += 1
        feedback.append("Lowercase letter check passed.")
    else:
        feedback.append("No lowercase letters found.")

    if has_digit:
        score += 1
        feedback.append("Number check passed.")
    else:
        feedback.append("No numbers found.")

    if has_special:
        score += 1
        feedback.append("Special character check passed.")
    else:
        feedback.append("No special characters found.")
    
    return score, feedback

#Start of program.
print("="*30)
print(" Password Strength Checker ")
print("="*30 + "\n")

while True:
    password = pwinput.pwinput(prompt="Enter password to check or type exit to quit: ", mask='*')

    if password.lower() == 'exit':
        print("Goodbye!")
        break

    #Common password check. If on the list, the rest of the loop is skipped.
    if password.lower() in common_pws:
        print("\nThis password is found in a list of commonly used passwords.")
        print("It is considered very weak and should not be used.\n")
        print("\n" + "="*30 + "\n")
        continue

    #Tally and report
    score, feedback = evaluate_pw(password)
    print()

    for line in feedback:
        print(line)

    print(f"\nPassword score: {score} out of 5.")
    if score == 5:
        print("This is a strong password.")
    elif score >= 3:
        print("This is a decent password.")
    else:
        print("This is a weak password.")

    print("\n" + "="*30 + "\n")
