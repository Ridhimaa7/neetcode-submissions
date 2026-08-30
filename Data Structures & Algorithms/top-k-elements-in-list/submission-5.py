import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = Counter(nums)
        return heapq.nlargest(k, c1.keys(), key = c1.get)