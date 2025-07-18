## Password Strength Checker (Python)

This Python script checks password strength based on five core rules and verifies whether the password has been exposed in known data breaches using the Have I Been Pwned API. 
It provides clear, structured console output and offers optional masked input.

---

## Features

- Five-rule password strength evaluation (length, upper/lowercase, digit, special character)  
- Real-time breach check using the HIBP API  
- Suggestions to improve weak passwords  
- Optional masked input via pwinput (fallbacks to getpass)  
- Looping interface for testing multiple passwords  
- Cross-platform compatibility (Python 3.x)  

---

## How to Use

1. Open a terminal
2. Navigate to the Python directory:
    cd path/to/Password-Strength-Checker/Python
3. Run the script:
    python PasswordStrengthChecker.py

Optional: Install pwinput for masked input with asterisks:
pip install pwinput
If not installed, the script defaults to getpass for secure input.

---

## Example Output

- Strong password  
Enter password to check or type exit to quit: ********  
Length check passed  
Uppercase letter check passed  
Lowercase letter check passed  
Number check passed  
Special character check passed  

Password score: 5 out of 5  
This is a strong password  

- Tips to improve a weak password
Password score: 2 out of 5.  
This is a weak password.  

Suggestions to improve your password:  
 - Make sure your password is at least 8 characters long.  
 - Include at least one special character (e.g., !, @, #).  

- If the input appeared in known data breaches.  
This password has appeared 45,310 known data breaches.  
It is strongly recommended that you do not use this as a password.  

---
