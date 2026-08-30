class Solution:
    def isValid(self, s: str) -> bool:
        closing = {'}':'{',']':'[',')':'('}
        stack = []
        for x in s:
            if x not in closing:
                stack.append(x)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if closing[x] != elem:
                    return False
        return not stack