class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r,c,memo):
            if r == R or c == C:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            if memo[r][c] > 0:
                return memo[r][c]
            memo[r][c] = dp(r,c + 1, memo) + dp(r + 1 , c , memo)
            return memo[r][c]
        R = m
        C = n
        memo = [[0]*C for _ in range(R)]
        return dp(0,0,memo)