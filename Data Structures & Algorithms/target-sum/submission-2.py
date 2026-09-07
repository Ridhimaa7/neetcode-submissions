class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i,running_sum,cache):
            #base case
            if i >=  len(nums):
                if running_sum == target:
                    return 1
                else:
                    return 0
            if (i,running_sum) in cache:
                return cache[(i,running_sum)]
            #choice1
            count1 = dp(i+1,running_sum-nums[i],cache)
            #choice2
            count2 = dp(i+1,running_sum + nums[i],cache)
            count = count1 + count2
            cache[(i,running_sum)] = count
            return cache[(i,running_sum)]
        return dp(0,0,{})
