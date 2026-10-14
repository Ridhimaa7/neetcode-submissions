import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxheap = [(-v,k) for k , v in c.items()]
        heapq.heapify(maxheap)
        queue = deque()
        time = 0
        while queue or maxheap:
            time += 1
            if maxheap:
                v , k = heapq.heappop(maxheap)
                if v + 1 != 0:
                    queue.append((v + 1, k , time + n))
            if queue:
                if queue[0][2] == time:
                    value = queue.popleft()[:2]
                    heapq.heappush(maxheap,value)
        return time
