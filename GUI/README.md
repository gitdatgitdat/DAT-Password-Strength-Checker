## GUI - Password Strength Checker

This directory contains the GUI implementation of the Password Strength Checker using Python's `tkinter` library.

## Overview

The graphical interface allows users to enter a password and evaluate its strength based on:
- Length and character complexity
- Whether it has been involved in known data breaches via the Have I Been Pwned (HIBP) API

Results are displayed with feedback and tips for improving password security.

## Features

- Clear, user-friendly interface
- HIBP integration to check for compromised passwords
- Real-time evaluation with score and improvement suggestions
- Auto-clears the password field after each check

## Requirements

- Python 3.x
- Internet connection (for HIBP API)

No third-party libraries are required unless you modify the project.

## How to Run

From the root project directory, run:

python GUI/PasswordStrengthGUI.py
