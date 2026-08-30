from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m = capacity
        n = len(weight)
        
        # Initialize the previous row for dynamic programming
        prevRow = [0] * (m + 1)
        
        # Process each item
        for i in range(n):
            currRow = [0] * (m + 1)
            for j in range(m + 1):
                if j < weight[i]:
                    currRow[j] = prevRow[j]  # Can't include this item
                else:
                    # Max profit by excluding or including the current item
                    currRow[j] = max(prevRow[j], profit[i] + prevRow[j - weight[i]])
            
            # After processing the current item, update prevRow
            prevRow = currRow
        
        # The answer is in prevRow, at the full capacity
        return prevRow[m]
