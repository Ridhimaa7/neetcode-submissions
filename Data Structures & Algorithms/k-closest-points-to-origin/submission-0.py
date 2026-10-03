import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            x1 = point[0]
            x2 = 0
            y1 = point[1]
            y2 = 0
            d = (x1 - x2)**2 + (y1 - y2)**2
            minheap.append((d,x1,y1))
        heapq.heapify(minheap)
        res = []
        for _ in range(k):
            d, x , y = heapq.heappop(minheap)
            res.append([x, y])
        return res