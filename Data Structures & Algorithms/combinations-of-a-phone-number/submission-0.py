class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        currComb = []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def helper(i,currComb):
            if len(currComb) == len(digits):
                result.append("".join(currComb))
                return
            if i >= len(digits):
                return
            scope = hashmap[digits[i]]
            for char in scope:
                currComb.append(char)
                helper(i+1,currComb)
                currComb.pop()
        helper(0,[])
        return result
            
        