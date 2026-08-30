class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1= {}
        l1 = [[] for i in range(0,len(nums)+1)]
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        for key , val in dict1.items():
            l1[val].append(key)
        result = []
        for i in range(len(l1)-1,0,-1):
            for n in l1[i]:
                result.append(n)
                if len(result) == k:
                    return result

        