#!/usr/bin/python3
"""
Prime Game - Who is the winner?
"""

def isWinner(x, nums):
    """Determine who the winner of the most rounds is"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        rounds_set = list(range(1, n + 1))
        primes_set = sieve_of_eratosthenes(n)

        if not primes_set:
            ben_wins += 1
            continue

        maria_turn = True

        while True:
            if not primes_set:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)

            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n"""
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return primes
