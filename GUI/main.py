import tkinter as tk
from tkinter import messagebox
import os
import sys

#Ensure path to root directory to access utils.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import evaluate_pw, pwned_password_check

def check_password():
    password = password_entry.get()
    result_box.delete("1.0", tk.END)

    if not password:
        result_box.insert(tk.END, "Please enter a password.\n")
        return
    
    if password.lower() == "exit":
        root.quit()
        return
    
    breach_count = pwned_password_check(password)
    if breach_count is None:
        result_box.insert(tk.END, "Error: Could not reach the breach database.\n")
        return
    elif breach_count > 0:
        result_box.insert(tk.END, f"This password has appeared in {breach_count:,} known data breaches.\n")
        result_box.insert(tk.END, "It is strongly recommended that you do not use this password.\n")
        return
    
    score, feedback, tips = evaluate_pw(password)

    result_box.insert(tk.END, "\n".join(feedback) + "\n\n")
    result_box.insert(tk.END, f"Password score: {score} out of 5.\n")

    if score == 5:
        result_box.insert(tk.END, "This is a strong password.\n")
    elif score >= 3:
        result_box.insert(tk.END, "This is a decent password.\n")
    else:
        result_box.insert(tk.END, "This is a weak password.\n")

    if tips:
        result_box.insert(tk.END, "\nSuggestions to improve your password:\n")
        for tip in tips:
            result_box.insert(tk.END, f" - {tip}\n")

    password_entry.delete(0, tk.END)

#Toggle visiblity of password
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else: 
        password_entry.config(show="*")

#GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter Password:").pack(anchor="w")
password_entry = tk.Entry(frame, show="*", width=40)
password_entry.pack(pady=(0, 10))
password_entry.focus()

#Track toggle visiblity checkbox state
show_password_var = tk.BooleanVar(value=False)

#Password visiblity checkbox
tk.Checkbutton(
    frame,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password
).pack(anchor="w")

tk.Button(frame, text="Check Password", command=check_password).pack()

result_box = tk.Text(frame, height=15, width=60)
result_box.pack(pady=(10, 0))

root.bind('<Return>', lambda event: check_password())
root.mainloop()