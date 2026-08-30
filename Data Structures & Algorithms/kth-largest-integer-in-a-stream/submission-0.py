class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        maxheap = [-x for x in self.nums]
        heapq.heapify(maxheap)
        for _ in range(self.k - 1):
            heapq.heappop(maxheap)

        return -(heapq.heappop(maxheap))
        
        
