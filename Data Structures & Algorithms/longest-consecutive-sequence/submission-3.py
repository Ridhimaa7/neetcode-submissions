class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set1 = set(nums)
        max_count = 0
        for num in set1:
            if num - 1 not in set1:
                curr_num = num
                count = 1
                while curr_num + 1 in set1:
                    count += 1
                    curr_num += 1
                max_count = max(max_count, count)
        return max_count