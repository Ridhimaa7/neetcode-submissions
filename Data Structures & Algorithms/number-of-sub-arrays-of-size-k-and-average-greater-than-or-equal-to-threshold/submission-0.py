class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        totalcount = 0
        l = 0
        total = 0
        for r in range(len(arr)):
            total += arr[r]
            if r - l + 1 > k:
                total -= arr[l]
                l = l + 1
            if r - l + 1 == k:
                if total / k >= threshold:
                    totalcount += 1
        return totalcount



        