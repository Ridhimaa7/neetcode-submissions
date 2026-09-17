class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixArray = []
        operator = 1
        postoperator = 1
        postfixArray = []
        for num in nums:
            prefixArray.append(num * operator)
            operator *= num
            if operator == 0:
                operator = 1
        for num in nums[::-1]:
            postfixArray.append(num * postoperator)
            postoperator *= num
            if postoperator == 0:
                postoperator = 1
        i = 0
        j = 0
        maxNum = float('-inf')
        for i in range(len(postfixArray)):
            if postfixArray[i] > maxNum:
                maxNum = postfixArray[i]
            if prefixArray[j] > maxNum:
                maxNum = prefixArray[j]
            j += 1
        return maxNum