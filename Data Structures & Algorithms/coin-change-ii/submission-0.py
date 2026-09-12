class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i,total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0 
            if (i,total) in cache:
                return cache[(i,total)]
            max_include = dfs(i,total+coins[i])
            skip = dfs(i+1,total)
            cache[(i,total)] = max_include + skip
            return cache[(i,total)]
        return dfs(0,0)

            