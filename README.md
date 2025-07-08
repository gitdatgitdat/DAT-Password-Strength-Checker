# Password Strength Checker (PowerShell)

This is a simple but effective script that evaluates the strength of a password based on common security guidelines. 
It's built in PowerShell and runs in a loop, allowing repeated checks until the user exits.

## Features

- Validates password strength based on five rules:
  - Minimum length (8 characters)
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- Outputs a score from 0 to 5
- Gives a strength rating (Weak, Moderate, Strong)
- Runs in a loop for continuous testing
- Clean, readable console output

## How to Use

1. Open PowerShell
2. Run the script
'''cd path\to\script
.\PasswordStrengthChecker.ps1'''
4. Enter a password when prompted.
5. View the individual check results and overall strength score.
6. Type exit when you’re done.

##Example Output

Enter password to check or type 'exit' to quit
MyPass123!

Length check passed
Uppercase letter check passed
Lowercase letter check passed
Number check passed
Special character check passed

Password score: 5 out of 5
This is a strong password

## Coming Soon

- Python version
- GUI wrapper
