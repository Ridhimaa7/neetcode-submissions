class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def dp(i):
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
            minimum = float("inf")
            for num in range(1, nums[i] + 1):
                minimum = min(minimum, 1 + dp(i + num))
            cache[i] = minimum
            return cache[i]

        return dp(0)