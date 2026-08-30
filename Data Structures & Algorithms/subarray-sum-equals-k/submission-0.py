class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0 : 1}
        total = 0
        res = 0
        for i in nums:
            total += i
            if total - k in prefixsum:
                res += prefixsum[total - k]
            prefixsum[total] = prefixsum.get(total, 0) + 1
        return res
        