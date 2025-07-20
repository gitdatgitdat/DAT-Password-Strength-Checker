## Password Strength Checker

A cross-platform password strength evaluation tool written in PowerShell and Python, now with an optional graphical interface. Each version checks password complexity and provides real-time feedback based on common security practices. The Python versions also integrate with Have I Been Pwned (HIBP) to detect breached passwords.

---

## Contents

- `PowerShell/` – PowerShell-based password checker
- `Python/` – Console-based Python password checker with breach checking
- `GUI/` – Graphical password checker built with Tkinter

Each version includes its own README with setup and usage details.

---

## Features

- Evaluates passwords against five core rules:
  - Minimum length (8 characters)
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
  - At least one special character
- Scores and rates password strength
- HIBP integration in Python versions to detect known data breaches
- Optional input masking in Python terminal version (via `pwinput`)
- Cross-platform support (Windows and Unix-like systems)
- Simple and responsive GUI interface with Tkinter

---

## Roadmap

- [x] Python version with external password breach check
- [x] Optional GUI via Tkinter
- [ ] Unit tests and CI integration
- [ ] Dark mode or theme toggle for GUI (optional future enhancement)
