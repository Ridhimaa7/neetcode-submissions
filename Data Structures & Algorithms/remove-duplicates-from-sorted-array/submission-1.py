class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        k = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[k] = nums[j]
                i = k
                k += 1
                j += 1
        return k