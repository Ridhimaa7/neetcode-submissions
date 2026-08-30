class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashdict = dict()
        for i in range(len(nums)):
            if nums[i] in hashdict.keys():
                if abs(i - hashdict[nums[i]]) <= k:
                    return True
            hashdict[nums[i]] = i
        return False




        
        