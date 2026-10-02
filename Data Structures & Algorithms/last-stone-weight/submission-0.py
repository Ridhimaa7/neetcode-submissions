import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) >= 2:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            res = abs(x) - abs(y)
            if abs(x) == abs(y):
                continue
            else:
                heapq.heappush(maxheap,-res)
        if maxheap:
            res = -heapq.heappop(maxheap)
        else:
            res = 0
        return res

        
