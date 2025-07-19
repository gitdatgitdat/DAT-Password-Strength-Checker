import re
import hashlib
import requests

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
            return None
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
        return 0
    except requests.RequestException:
        return None