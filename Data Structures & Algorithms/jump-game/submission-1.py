class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dp(i):
            if i == len(nums) - 1:
                return True
            if i >= len(nums) or nums[i] == 0:
                return False
            if i in cache:
                return cache[i]
            for num in range(1,nums[i] + 1):
                if dp(i + num):
                    cache[i] = True
                    return True
            cache[i] = False
            return cache[i]
        return dp(0)

        