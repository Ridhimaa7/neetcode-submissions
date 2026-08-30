class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrak(i, nums, currset, subset):
            if i >= len(nums):
                subset.append(currset.copy())
                return
            currset.append(nums[i])
            backtrak(i+1, nums, currset, subset)
            currset.pop()
            backtrak(i+1, nums, currset, subset)
            return subset
        return backtrak(0,nums,[],[])