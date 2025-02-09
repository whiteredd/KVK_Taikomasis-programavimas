num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
    remainder = num1 % num2
else:
    division = "Undefined "
    remainder = "Undefined "


if num1 == 0 and num2 == 0:
    power = "Undefined "
elif num1 == 0 and num2 < 0:
    power = "Error"
else:
    power = num1 ** num2


print(f"\nResults:")     # \n creates a new line
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {remainder}")
print(f"{num1} ** {num2} = {power}")
