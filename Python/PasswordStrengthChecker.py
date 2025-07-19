import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import evaluate_pw, pwned_password_check

#Pull in pwinput if its available, otherwise use getpass.
try:
    import pwinput
    use_pwinput = True
except ImportError:
    import getpass
    use_pwinput = False

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
    #Replaced by HIBP check for stronger validation.
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
