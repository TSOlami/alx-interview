#!/usr/bin/python3
"""Solving the Prime Game"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def calculate_primes(n):
    """
    Calculate prime numbers up to n.

    Args:
        n (int): The maximum number to calculate primes up to.

    Returns:
        list: List of prime numbers.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing
        the values of n for each round.

    Returns:
        str or None: The name of the player with
        the most wins or None if it cannot be determined.
    """
    def play_game(n):
        if n == 1:
            return "Ben"
        primes = calculate_primes(n)
        if len(primes) % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
