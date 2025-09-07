def is_perfect_number(n):
    # Check if the number is positive
    if n <= 0:
        return False

    # Find the sum of proper divisors
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    # Check if the sum of divisors equals the number
    return divisors_sum == n

# Test the function
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")