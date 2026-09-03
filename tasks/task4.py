def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def twin_primes(limit=1000):
    result = []
    for i in range(3, limit - 2, 2):
        if is_prime(i) and is_prime(i + 2):
            result.append((i, i + 2))
    return result


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


def dec_to_bin(n):
    return bin(n)[2:]


def perfect_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        if num > 0:
            divisors_sum = sum(
                i for i in range(1, num) if num % i == 0
            )
            if divisors_sum == num:
                result.append(num)
    return result


print("Multiplication table of 5:")
print_multiplication_table(5)

print("\nTwin primes under 100:")
print(twin_primes(100))

print("\nPrime factors of 56:")
print(prime_factors(56))

print("\nDecimal 25 to binary:")
print(dec_to_bin(25))

print("\nPerfect numbers between 1 and 500:")
print(perfect_numbers(1, 500))