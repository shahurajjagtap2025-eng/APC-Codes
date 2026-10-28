def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication
x, y, z = calculate(20, 5)
print("Addition =", x)
print("Subtraction =", y)
print("Multiplication =", z)

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
number = int(input("Enter a number: "))
print(check_number(number))




