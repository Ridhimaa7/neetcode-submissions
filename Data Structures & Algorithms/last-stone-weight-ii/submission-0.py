class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = math.ceil(sum(stones) / 2)
        def dfs(i,total):
            if i>= len(stones) or total >= target:
                val = sum(stones) - total
                return abs(val - total)
            if (i,total) in cache:
                return cache[(i,total)]
            val = min(dfs(i+1, total + stones[i]) , dfs(i+1,total))
            cache[(i,total)] = val
            return cache[(i,total)]
        cache = {}
        return dfs(0,0)