class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        L = 0
        curMax = 0
        if s == " " or len(s) == 1:
            return 1
        for R in range(len(s)):
            while s[R] in hashset:
                curMax = max(curMax , R - L)
                hashset.remove(s[L])
                L += 1
            hashset.add(s[R])
            curMax = max(curMax , R - L + 1)
        return curMax

        