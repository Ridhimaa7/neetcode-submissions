import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c1 = Counter(tasks)
        maxheap = [(-v,k) for (k,v) in c1.items()]
        heapq.heapify(maxheap)
        queue = deque()
        list1 = []
        time = 0
        while maxheap or queue:
            time += 1
            if maxheap:
                v,k = heapq.heappop(maxheap)
                list1.append(k)
                if abs(v) - 1 > 0:
                    queue.append((k,abs(v) - 1 , time + n))
            else:
                list1.append("Idle")
            if queue and queue[0][2] == time:
                key , val , t = queue.popleft() 
                heapq.heappush(maxheap,(-val,key))
        return time