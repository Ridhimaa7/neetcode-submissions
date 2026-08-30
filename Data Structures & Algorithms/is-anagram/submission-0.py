from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict1 = Counter(s)
            dict2 = Counter(t)
            if dict1 == dict2:
                return True
            else:
                return False