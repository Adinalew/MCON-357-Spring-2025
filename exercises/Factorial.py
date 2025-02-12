#Adina Lew
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("Factorial Computation Using Recursion")

    while True:
        try:
            integer = int(input("Enter a non-negative integer: "))
            if integer < 0:
                print("Input Error. Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    factorial_answer = factorial_recursive(integer)
    print(f"The factorial of {integer} is: {factorial_answer}")

if __name__ == "__main__":
    main()
