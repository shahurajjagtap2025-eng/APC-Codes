# 11 develop a sign-up website
import re

def is_valid_email(email):
    pattern = r'^[A-Z a-z 0-9._-]+@[A-Z a-z 0-9]+(?:\.[A-Z a-z 0-9]+)*\.[A-Z a-z]{2,6}$'
    return bool(re.fullmatch(pattern, email))

email = input("Enter your email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")