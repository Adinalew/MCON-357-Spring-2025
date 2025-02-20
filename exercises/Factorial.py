# Adina Lew
import sys

def process_input(input_str):
    try:
        value = int(input_str)
        if value < 0:
            return None, 'Number cannot be negative'
        return value, None
    except ValueError:
        return None, "Invalid input. Number must be a valid integer."

def factorial_recursive(n, recursive_limit, recursive_count=0):
    if check_recursion_limit(recursive_count, recursive_limit) is True:
        return None

    if n == 0 or n == 1:
        return 1
    result = factorial_recursive(n - 1, recursive_limit, recursive_count + 1)

    if result is None:
        return None

    return n * result

def check_recursion_limit(recursive_count, recursive_limit):
    if recursive_count >= recursive_limit:
        return True
    return False

def main():
    print(f"Factorial Computation Using Recursion - Recursion Limit: {sys.getrecursionlimit()}")
    recursive_limit = sys.getrecursionlimit() - 4 #needed to be lowered because Python stores another limit with a smaller value

    while True:
        integer_str = input("Enter a non-negative integer: ")
        integer, error_message = process_input(integer_str)
        if error_message:
            print(error_message)
        else:
            break

    factorial_answer = factorial_recursive(integer, recursive_limit)
    if factorial_answer is None:
        print("Exceeded limit. Could not get output of factorial")
    else:
        print(f"The factorial of {integer} is: {factorial_answer}")

if __name__ == "__main__":
    main()
