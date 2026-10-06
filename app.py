# Simple Greeting and Calculator Program

def greet_user():
    print("Welcome to my GitHub portfolio!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you.")

def simple_calculator():
    print("\n--- Mini Calculator ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {sum_result}")

if __name__ == "__main__":
    greet_user()
    simple_calculator()
