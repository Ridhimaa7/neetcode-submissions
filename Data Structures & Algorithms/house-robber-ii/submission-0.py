class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            cache = {}
            def dfs(i):
                if i >= len(arr):
                    return 0
                if i in cache:
                    return cache[i]
                cache[i] = max(dfs(i+1), arr[i] + dfs(i+2))
                return cache[i]
            return dfs(0)
        return max(helper(nums[:-1]), helper(nums[1:]))