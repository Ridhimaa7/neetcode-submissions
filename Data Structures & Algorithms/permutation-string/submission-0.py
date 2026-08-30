class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        if k > len(s2): return False
        target = Counter(s1)
        for i in range(len(s2) - k + 1):
            window = s2[i:i+k]
            if Counter(window) == target:
                return True
        return False