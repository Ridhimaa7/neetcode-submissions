class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        set1 = set()
        list1 = []
        for i in range(len(nums)):
            if target - nums[i] in set1:
                list1 = [dict1[target - nums[i]], i]
                break
            dict1[nums[i]] = i
            set1.add(nums[i])
        return sorted(list1)