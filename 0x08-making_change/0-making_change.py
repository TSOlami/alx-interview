#!/usr/bin/python3
"""
"""

def makeChange(coins, total):
    if total < 0:
        return -1

    # Initialize a table to store the minimum number
	# of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the minimum number of coins needed
	# for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'),
	# it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
