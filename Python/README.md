## Password Strength Checker (Python)

This Python script checks password strength based on five rules and offers clear, readable console output. It supports optional input masking using the `pwinput` module.

---

## Features

- Five-rule strength evaluation
- Masked input (if `pwinput` is installed)
- Looping password checks
- Clean, spaced output formatting
- Compatible with both Python 3.x and most terminal environments

---

## How to Use

1. Open a terminal
2. Navigate to the Python directory:
    cd path/to/Password-Strength-Checker/Python

3. Run the script:
    python PasswordStrengthChecker.py

If you’d like to see asterisks while typing your password, install:
pip install pwinput

Otherwise the script will default to unmasked input using getpass if pwinput is unavailable.

---

## Example Output

Enter password to check or type exit to quit: ********  
Length check passed  
Uppercase letter check passed  
Lowercase letter check passed  
Number check passed  
Special character check passed  

Password score: 5 out of 5  
This is a strong password  

---
