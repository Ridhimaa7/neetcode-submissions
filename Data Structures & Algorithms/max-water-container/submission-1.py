class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        maxArea = 0
        while L < R:
            maxArea = max(maxArea , ((R - L) * min(heights[L],heights[R])))
            if heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R  -= 1
            else:
                R -= 1
                L += 1
        return maxArea
        