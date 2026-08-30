class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = []
        output = []
        mul = 1
        for i in range(len(nums)):
            mul = mul * nums[i]
            prefixArray.append(mul)
        
        suffix_mul = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix = prefixArray[i-1] if i > 0 else 1
            output.insert(0, prefix * suffix_mul)
            suffix_mul *= nums[i]
        return output