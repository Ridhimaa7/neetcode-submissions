class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + dp(i+2, cache), dp(i+1, cache))
            return cache[i]
        return dp(0, {})