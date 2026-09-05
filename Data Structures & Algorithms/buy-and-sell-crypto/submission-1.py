class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_min = prices[0]
        global_max = 0
        for i in range(len(prices)):
            if prices[i] > global_min:
                global_max = max(global_max, prices[i] - global_min)
            else:
                global_min = prices[i]
        return global_max
