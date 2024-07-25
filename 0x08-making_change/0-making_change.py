#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin

    return count if total == 0 else -1
