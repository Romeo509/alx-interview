#!/usr/bin/python3
"""
Prime Game - Who is the winner?
"""


def is_prime(n):
    """ Helper function to check if a number is prime """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """ Generate list of prime numbers up to n using
    the Sieve of Eratosthenes """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def play_round(n, primes):
    """ Simulate a round and determine the winner """
    primes_in_round = [i for i in range(1, n + 1) if primes[i]]
    return len(primes_in_round) % 2 == 1


def isWinner(x, nums):
    """ Determine who the winner of the most rounds is """
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
