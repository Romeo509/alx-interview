#!/usr/bin/python3
"""Prime Game - Determine the winner of a prime number removal game."""


def isWinner(x, nums):
    """Determine who wins the most rounds."""
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0  # Initialize Ben's win counter
    maria_wins = 0  # Initialize Maria's win counter

    max_num = max(nums)  # Find the maximum number in nums

    sieve = [1] * (max_num + 1)  # Create a list to mark prime numbers

    sieve[0], sieve[1] = 0, 0  # Mark 0 and 1 as non-prime

    for i in range(2, len(sieve)):
        if sieve[i] == 1:  # If i is a prime number
            remove_multiples(sieve, i)  # Mark its multiples as non-prime

    for num in nums:
        if sum(sieve[:num + 1]) % 2 == 0:  # Ben wins if primes are even
            ben_wins += 1
        else:  # Maria wins if primes are odd
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def remove_multiples(sieve, prime):
    """Mark multiples of the given prime number as non-prime."""
    for i in range(2, len(sieve)):
        try:
            sieve[i * prime] = 0  # Set multiples of prime to 0
        except (IndexError, ValueError):
            break
