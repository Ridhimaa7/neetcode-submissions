class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dp(i,amount):
            if i >= len(nums):
                return amount
            if (i,amount) in cache:
                return cache[(i,amount)]
            skip = dp(i+1,amount)
            take = dp(i+2,amount + nums[i])
            cache[(i,amount)] = max(skip,take)
            return cache[(i,amount)]
        return dp(0,0)
        