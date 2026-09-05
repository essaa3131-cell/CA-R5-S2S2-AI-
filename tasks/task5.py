class MathUtils:

    def __init__(self, number):
        self.number = number

    def get_multiplication_table(self):
        return [
            f"{self.number} * {i} = {self.number * i}"
            for i in range(1, 11)
        ]

    def get_prime_factors(self):
        n = self.number
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

    def to_binary(self):
        return bin(self.number)[2:]


class NumberSequence:

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_twin_primes(self, limit=1000):
        result = []
        for i in range(3, limit - 2, 2):
            if self.is_prime(i) and self.is_prime(i + 2):
                result.append((i, i + 2))
        return result

    def get_perfect_numbers(self, start, end):
        result = []
        for num in range(start, end + 1):
            if num > 0:
                divisors_sum = sum(
                    i for i in range(1, num) if num % i == 0
                )
                if divisors_sum == num:
                    result.append(num)
        return result


math_obj = MathUtils(56)
print("Prime factors of 56:", math_obj.get_prime_factors())
print("56 in binary:", math_obj.to_binary())

seq_obj = NumberSequence()
print("Twin primes under 100:", seq_obj.get_twin_primes(100))
print(
    "Perfect numbers between 1 and 500:",
    seq_obj.get_perfect_numbers(1, 500),
)