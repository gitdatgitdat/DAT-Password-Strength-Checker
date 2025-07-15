## Password Strength Checker (PowerShell)

A simple yet effective PowerShell script to evaluate the strength of a password using basic security principles. 
It checks for character variety, detects commonly used passwords, and offers tips to improve weak entries.

---

## Features

- Checks password strength based on five core rules:
  - Minimum length (8 characters)
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- Detects commonly used passwords (based on `common-passwords.txt`)
- Normalizes input by removing whitespace and ignoring capitalization for comparison
- Provides a score (0–5) and a strength rating (Weak, Decent, Strong)
- Offers helpful suggestions for weak passwords
- Clean, user-friendly looped interface
- Lightweight and easy to run locally

---

## How to Use

1. Open PowerShell  
2. Navigate to the script folder  
   cd path\to\script
3. Run the script
   .\PasswordStrengthChecker.ps1
4. Enter a password when prompted
5. Review feedback and tips
6. Type exit at any time to quit

---

## Requirements

PowerShell 5.0 or higher (Windows, Linux, or macOS)  
common-passwords.txt file in the same directory as the script  

---

## Example Output

Password Strength Checker  

Enter password to check or type 'exit' to quit: booger  
Password is too short (Minimum 8 characters)  
No uppercase letters found  
Lowercase letter check passed  
No numbers found  
No special characters found  

Password score: 1 out of 5  
This is a weak password  

Tip: Make your password at least 8 characters long.  
Tip: Add at least one number.  
Tip: Add at least one special character (e.g., !, @, #).  

---

## Roadmap

Python version using zxcvbn or passlib for improved scoring  
GUI wrapper  
Input masking  
Integration with clipboard safety checks  

---
