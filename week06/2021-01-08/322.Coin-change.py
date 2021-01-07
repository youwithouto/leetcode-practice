class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] > amount else dp[amount]
