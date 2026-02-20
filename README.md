# password-strength-checker

A simple Python CLI application that evaluates the strength of a password based on security rules.

## Features

- Checks minimum length
- Detects uppercase letters
- Detects lowercase letters
- Detects digits
- Detects special characters
- Returns strength rating (Weak, Medium, Strong, Very Strong)

## How It Works

The program scans each character in the password and validates it using Python string methods such as:
- isupper()
- islower()
- isdigit()
- isalnum()

A scoring system is used to determine the overall strength.

## How to Run

1. Clone the repository
2. Navigate into the folder
3. Run:
