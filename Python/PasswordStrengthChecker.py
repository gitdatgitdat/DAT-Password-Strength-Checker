import re
import os
import hashlib
import requests

#Load common passwords from the file one level up.
#Blocked out for HIBP check.
#common_pws_path = os.path.join(os.path.dirname(__file__), '..', 'common-passwords.txt')

#try:
    #with open(common_pws_path, 'r') as file:
        #common_pws = set(p.strip().lower() for p in file)
#except FileNotFoundError:
    #print("Warning: common-passwords.txt not found. Skipping weak password check.")
    #common_pws = set()

#Pull in pwinput if its available, otherwise use getpass.
try:
    import pwinput
    use_pwinput = True
except ImportError:
    import getpass
    use_pwinput = False

#Function for evaluating the given password.
def evaluate_pw(password):
    score = 0
    feedback = []
    tips = []

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
        tips.append("Tip: Make sure your password is at least 8 characters long.")

    if has_upper:
        score += 1
        feedback.append("Uppercase letter check passed.")
    else:
        feedback.append("No uppercase letters found.")
        tips.append("Tip: Include at least one uppercase letter.")

    if has_lower:
        score += 1
        feedback.append("Lowercase letter check passed.")
    else:
        feedback.append("No lowercase letters found.")
        tips.append("Tip: Include at least one lowercase letter.")

    if has_digit:
        score += 1
        feedback.append("Number check passed.")
    else:
        feedback.append("No numbers found.")
        tips.append("Tip: Add at least one number.")

    if has_special:
        score += 1
        feedback.append("Special character check passed.")
    else:
        feedback.append("No special characters found.")
        tips.append("Tip: Add at least one special character (e.g., !, @, #).")
    
    return score, feedback, tips

#Function to see if given password appears in pwnedpasswords database.
def pwned_password_check(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print("Error checking password breach status.")
            return 0
        
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
        
        return 0
    except requests.RequestException:
        print("Network error while checking password breach status.")
        return 0

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
    #Blocked for HIBP check.
    #if password.lower() in common_pws:
        #print("\nThis password is found in a list of commonly used passwords.")
        #print("It is considered very weak and should not be used.\n")
        #print("\n" + "="*30 + "\n")
        #continue

    breach_count = pwned_password_check(password)
    if breach_count > 0:
        print(f"\nThis password has appeared {breach_count:,} known data breaches.")
        print("It is strongly recommended that you do not use this as a password. \n")
        print("\n" + "="*30 + "\n")
        continue

    #Tally and report
    score, feedback, tips = evaluate_pw(password)
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

    if tips:
        print("\nSuggestions to improve your password.")
        for tip in tips:
            print(f" - {tip}")

    print("\n" + "="*30 + "\n")
