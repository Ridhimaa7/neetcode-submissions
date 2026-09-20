class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def helper(i, prev_idx):
            if i >= len(nums):
                return 0
            if (i, prev_idx) in cache:
                return cache[(i, prev_idx)]
            
            # Skip current element
            res = helper(i + 1, prev_idx)
            
            # Take current element if strictly greater than previous
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                res =  max(res,1 + helper(i + 1, i))
                
            cache[(i, prev_idx)] = res
            return res
            
        return helper(0, -1)