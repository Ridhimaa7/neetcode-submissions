class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        k = 0
        for j in range(len(nums)):
            if nums[j] == val:
                continue
            else:
                nums[k] = nums[j]
                k +=  1
        return len(nums[:k])
        