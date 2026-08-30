import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        list1 = []
        while nums:
            elem = heapq.heappop(nums)
            list1.append(elem)

        return list1