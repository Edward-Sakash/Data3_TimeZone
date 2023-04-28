"""while True:
    try:
        num = float(input("Enter a number that should divide 1: "))
        result = 1 / num
        print(f"1 divided by {num} is {result}")
        break
    except ZeroDivisionError:
        print("Error: You cannot divide by zero. Please enter a non-zero number.")
"""
# add else

while True:
    try:
        number = int(input("Enter a number to divide 1: "))
        result = 1 / number
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero number.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
    else:
        print("Result: ", result)
        break
