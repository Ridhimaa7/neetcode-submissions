class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        curmin = float('inf')
        curSum = 0
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                curmin = min(curmin, R - L + 1)
                curSum -= nums[L]
                L += 1
            if curSum == target:
                curmin = min(curmin, R - L + 1)
        if curmin == float("inf"):
            return 0
        else:
            return curmin
        