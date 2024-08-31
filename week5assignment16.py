prime = int(input("Enter a positive integer: "))

def is_prime(n):
    # Check if the number is less than or equal to 1
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Prompt the user to enter a number
    n = int(input("Enter a positive integer: "))
    # Check if the number is prime
    result = is_prime(n)
    # Print the result
    if result:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

if __name__ == '__main__':
    main()