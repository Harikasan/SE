import math

def perform_addition(a, b):
    return a + b

def perform_subtraction(a, b):
    return a - b

def perform_multiplication(a, b):
    return a * b

def perform_division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def calculate_square_root(a):
    if a < 0:
        raise ValueError("Square root of negative numbers is not real.")
    return math.sqrt(a)

operations = {
    "1": ("Addition", perform_addition),
    "2": ("Subtraction", perform_subtraction),
    "3": ("Multiplication", perform_multiplication),
    "4": ("Division", perform_division),
    "5": ("Square Root", calculate_square_root)
}

def display_menu():
    print("Calculator Menu:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Select operation (1-5): ")

        if choice not in operations:
            print("Invalid selection. Please try again.")
            continue

        operation_name, operation_func = operations[choice]

        try:
            if choice == "5":
                num = get_user_input("Enter a number: ")
                result = operation_func(num)
                print(f"{operation_name} of {num} = {result}")
            else:
                num1 = get_user_input("Enter first number: ")
                num2 = get_user_input("Enter second number: ")
                result = operation_func(num1, num2)
                print(f"{num1} {operation_name} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")

        if input("Perform another calculation? (yes/no): ").lower() != "yes":
            break

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()
