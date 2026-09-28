class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(i,cost_val):
            if i >= len(cost):
                return cost_val

            if (i,cost_val) in cache:
                return cache[(i,cost_val)]
            path1 = dp(i+1,cost_val + cost[i])
            path2 = dp(i+2, cost_val + cost[i])
            cache[(i,cost_val)] = min(path1,path2)
            return cache[(i,cost_val)]
        res = min(dp(0,0) , dp(1,0))
        return res

        