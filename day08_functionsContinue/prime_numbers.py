# Prime number checker
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            # Not a prime number
            print(f"The number {number} is not a prime number.")
            return
    # Prime number
    print(f"The number {number} is a prime number.")


print("-----------------------------")
is_prime(23)

print("-----------------------------")
is_prime(22)
