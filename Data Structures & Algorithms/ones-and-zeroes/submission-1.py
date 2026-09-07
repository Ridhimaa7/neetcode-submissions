class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        def dp(i,zero,ones):
            if i >= len(strs):
                return 0
            if (i,zero,ones) in cache:
                return cache[(i,zero,ones)]
            not_take = dp(i+1,zero,ones)
            take = 0
            count_zero = strs[i].count('0')
            count_one = strs[i].count('1')
            if m >= count_zero + zero and n >= count_one + ones:
                take = 1 + dp(i+1,zero + count_zero,ones + count_one)
            cache[(i,zero,ones)] = max(take,not_take)
            return cache[(i,zero,ones)]
        return dp(0,0,0)