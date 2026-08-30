class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        ans = []
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        # Sort dictionary items by value (frequency) in descending order
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        # Take the keys of the first k items
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res