class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashset = {}
        L = 0
        maxLength = 0
        maxFreq = 0
        for R in range(len(s)):
            hashset[s[R]] = hashset.get(s[R], 0) + 1
            maxFreq = max(maxFreq, hashset[s[R]])
            replacement = (R - L + 1) - maxFreq
            while (R - L + 1) - maxFreq > k:
                hashset[s[L]] = hashset.get(s[L],0) - 1
                L += 1
            maxLength = max(maxLength , R - L + 1)
        return maxLength