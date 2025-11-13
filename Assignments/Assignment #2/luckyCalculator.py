# Guillermo Montiel             09/19/2025
# Assignment: Lucky Calculator!
#
# This program works like a basic calculator that supports seven
# mathematical operations (+, -, *, /, //, %, **). It also allows
# the user to generate a random "lucky number" between two integers.
# The program handles divide-by-zero cases gracefully by adjusting
# the divisor and printing an error message instead of crashing.

import random

def print_header():
    print("Lucky Calculator!")
    print("By:Guillermo Montiel")
    print("[COM S 1270]")
    
def run_calculator():
    op = input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ")

    if op not in ["+", "-", "*", "/", "//", "%", "**"]:
        print('ERROR: You must enter either "+", "-", "*", "/", "//", "%", or "**"')
        return

    a = int(input("Please Enter An Integer: "))
    b = int(input("Please Enter An Integer: "))

    if b == 0 and op in ["/", "//", "%"]:
        print(f"ERROR in {op} Function: b = 0")
        b = 1  

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    elif op == "//":
        result = a // b
    elif op == "%":
        result = a % b
    elif op == "**":
        result = a ** b

    print(f"The result of your calculation was: {result}")

def lucky_number():
    low = int(input("Please Enter An Integer: "))
    high = int(input("Please Enter An Integer: "))
    num = random.randint(low, high)
    print(f"Your lucky number is: {num}")

def main():
    while True:
        print_header()
        choice = input("What would you like to do?\n[c]alculator, [l]ucky number, [q]uit: ")

        if choice == "c":
            run_calculator()
        elif choice == "l":
            lucky_number()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("ERROR: I did not understand your input... Please try again...")


if __name__ == "__main__":
    main()
