class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        Cmax , Cmin = 0, 0
        Gmax, Gmin = nums[0] , nums[0]
        Total = 0
        for n in nums:
            Cmax = max (Cmax + n , n)
            Gmax = max(Cmax,Gmax)
            Cmin = min(Cmin + n, n)
            Gmin = min(Gmin, Cmin)
            Total += n
        if Gmax < 0:
            return Gmax
        else:
            return max(Gmax, Total - Gmin)
        