class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = nums[0]
        for n in nums:
            currsum = max(currsum,0)
            currsum = currsum + n
            maxsum = max(currsum,maxsum)
        return maxsum
        