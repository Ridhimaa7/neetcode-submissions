class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for char in s:
            dict1[char] += 1 
        for char in t:
            dict2[char] += 1
        if dict1 == dict2:
            return True
        else:
            return False
        