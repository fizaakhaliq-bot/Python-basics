# Odd or Even Number Checker

def check_odd_even():
    print("--- Odd or Even Checker ---")
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"The number {num} is Even.")
        else:
            print(f"The number {num} is Odd.")
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    check_odd_even()
