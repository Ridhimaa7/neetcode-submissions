class Solution:
    def climbStairs(self, n: int) -> int:
        target = n
        cache = {}
        def dp(n):
            if n == target:
                return 1
            if n > target:
                return 0
            if n in cache:
                return cache[n]
            total = dp(n+1) + dp(n+2)
            cache[n] = total
            return cache[n]
        return dp(0)