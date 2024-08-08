#!/usr/bin/python3
"""
Prime Game - Who is the winner?
"""

def isWinner(x, nums):
    """
    Determine the winner of a set of prime number removal games.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of integers where each integer n denotes
        a set of consecutive integers starting from 1 up to and including n.

    Returns:
        str: The name of the player who won the most rounds ("Ben" or "Maria").
        None: If the winner cannot be determined.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    max_num = max(nums)
    sieve = [1] * (max_num + 1)
    sieve[0], sieve[1] = 0, 0  # 0 and 1 are not prime numbers

    # Generate prime numbers using Sieve of Eratosthenes
    for i in range(2, len(sieve)):
        if sieve[i] == 1:
            remove_multiples(sieve, i)

    # Play each round
    for num in nums:
        if sum(sieve[:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None

def remove_multiples(sieve, prime):
    """
    Mark multiples of a prime number as non-prime in the sieve.

    Args:
        sieve (list of int): Array where prime indices are 1 and non-prime indices are 0.
        prime (int): Prime number to mark multiples of.

    Returns:
        None.
    """
    for i in range(2, len(sieve)):
        try:
            sieve[i * prime] = 0
        except (IndexError, ValueError):
            break
