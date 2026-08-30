class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixArray = []
        initial = 0
        for num in nums:
            self.prefixArray.append(num + initial)
            initial += num
        
        

    def sumRange(self, left: int, right: int) -> int:
        rightVal = self.prefixArray[right]
        leftVal = self.prefixArray[left - 1] if left > 0 else 0
        return rightVal - leftVal
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)