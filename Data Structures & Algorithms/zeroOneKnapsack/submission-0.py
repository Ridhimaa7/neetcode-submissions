class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m  = capacity
        n = len(weight)
        dp = [[0] * (m + 1) for i in range(n) ] 
        for i in range(n):
            dp[i][0] = 0
        for i in range(m + 1):
            if i >= weight[0]:
                dp[0][i] = profit[0]
        for i in range(1,n):
            for j in range(1,m+1):
                skip = dp[i-1][j]
                include = 0 
                if j - weight[i] >= 0 :
                    include = profit[i] + dp[i-1][j - weight[i]]
                dp[i][j] = max(include , skip)
        return dp[n-1][m]


