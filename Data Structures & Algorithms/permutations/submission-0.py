class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        res = []
        visited = set()
        def dfs():
            if len(current) == len(nums):
                res.append(current.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                else:
                    current.append(num)
                    visited.add(num)
                    dfs()
                    current.pop()
                    visited.remove(num)
        dfs()
        return res