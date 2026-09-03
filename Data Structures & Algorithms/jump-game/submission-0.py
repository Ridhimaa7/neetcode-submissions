class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i,cache):
            if i == len(nums) - 1:
                return True
            if i in cache:
                return cache[i]
            
            end = min(len(nums) - 1 , i + nums[i])
            # Iterate backwards to find the goal faster and avoid depth issues
            for j in range(end, i, -1):
                if dfs(j, cache):
                    cache[i] = True
                    return True
            
            cache[i] = False
            return False
        return dfs(0, {})