class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxDict = {}
        for num in nums:
            if num in maxDict:
                maxDict[num] += 1
            else:
                maxDict[num] = 1
        for key , val in maxDict.items():
            if val > len(nums)/2:
                return key
        