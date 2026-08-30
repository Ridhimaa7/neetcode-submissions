class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = 10000000
        newL = 0
        newR = 0
        L = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLength = min(r-L+1,minLength)
                total -= nums[L]
                L += 1
        return minLength if minLength != 10000000 else 0
                


            

        