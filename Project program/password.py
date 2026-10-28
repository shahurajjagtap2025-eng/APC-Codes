#  14.password strength checker
import re

def is_strong_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_-]).{8,}$'
    return bool(re.fullmatch(pattern, password))

password = input("Enter your password: ")

if is_strong_password(password):
    print("Strong password")
else:
    print("Weak paswsword.")
