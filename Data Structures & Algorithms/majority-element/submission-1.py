class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashdict = {}
        n = len(nums)
        target = n / 2
        for num in nums:
            if num not in hashdict:
                hashdict[num] = 1
            else:
                hashdict[num] = hashdict.get(num,0) + 1
        for key, val in hashdict.items():
            if val > target:
                return key


        