class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = []
        L = 0
        if len(height) <= 1:
            return 0

        for R in range(1,len(height)):
            if height[R] >= height[L]:
                length = min(height[L], height[R])
                breadth = R - L - 1
                difference = 0
                temp_L = L
                while temp_L < R - 1:
                    temp_L += 1
                    difference += height[temp_L]
                area = length * breadth - difference

                arr1.append(max(0, area))
                L = R
        
        # Process from right to left to catch remaining water
        last_tall_idx = L
        L = len(height) - 1
        for R in range(len(height) - 2, last_tall_idx - 1, -1):
            if height[R] > height[L]:
                length = min(height[L], height[R])
                breadth = L - R - 1
                difference = 0
                temp_L = L
                while temp_L > R + 1:
                    temp_L -= 1
                    difference += height[temp_L]
                area = length * breadth - difference
                arr1.append(max(0, area))
                L = R
        return sum(arr1)