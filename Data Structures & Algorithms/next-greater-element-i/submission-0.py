class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numToidx = {num : idx for idx, num in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)
        for curr in nums2:
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = numToidx[val]
                res[idx] = curr
            if curr in numToidx:
                stack.append(curr)
        return res


        