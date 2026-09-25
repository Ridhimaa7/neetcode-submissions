class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        r = len(s) - 1
        l = 0
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        