class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        for n in range(0,len(nums) + 1):
            if n not in hashset:
                return n
        
                