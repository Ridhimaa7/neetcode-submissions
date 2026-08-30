class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currList =  []
        res = []
        def total(i,currList):
            if i >= len(nums):
                res.append(currList.copy())
                return
            currList.append(nums[i])
            total(i+1,currList)
            currList.pop()
            total(i+1,currList)
        total(0,currList)
        return res
        