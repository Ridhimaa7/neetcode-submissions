import heapq
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = list(nums)
        heapq.heapify(temp)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(temp)
        return nums