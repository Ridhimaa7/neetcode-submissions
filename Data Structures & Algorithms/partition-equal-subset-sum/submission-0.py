class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(i,running_sum,target,cache):
            if i >= len(nums):
                if running_sum == target:
                    return True
                else:
                    return False
            if (i,running_sum) in cache:
                return cache[(i,running_sum)]
            choice1 = dp(i+1,running_sum + nums[i], target, cache)
            choice2 = dp(i+1, running_sum, target, cache)
            cache[(i,running_sum)] = choice1 or choice2
            return cache[(i,running_sum)]
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums) // 2
            return dp(0,0,target,{})


        