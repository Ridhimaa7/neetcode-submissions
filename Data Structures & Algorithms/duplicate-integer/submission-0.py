class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = []
        for i in nums:
            if i not in l1:
                l1.append(i)
            else:
                return True
        return False
         