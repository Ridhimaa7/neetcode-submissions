class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(i,amt):
            if amt > amount or i >= len(coins):
                return float("inf")
            if amt == amount:
                return 0
            if (i,amt) in cache:
                return cache[(i,amt)]
            take = 1 + dp(i,amt + coins[i])
            not_take = dp(i+1,amt)
            cache[(i,amt)] = min(take,not_take)
            return cache[(i,amt)]
        res = dp(0,0)
        return res if res != float("inf") else -1