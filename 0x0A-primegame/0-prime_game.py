#!/usr/bin/python3
"""Module for solving the prime game question."""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: The name of the player that won the most rounds,
    or None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    is_prime = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False
    is_prime[0] = is_prime[1] = False

    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    maria_wins = 0
    for num in nums:
        maria_wins += is_prime[num] % 2 == 1

    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
