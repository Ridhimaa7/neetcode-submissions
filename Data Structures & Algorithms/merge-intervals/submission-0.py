class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]] #[[1,3]]
        for index in range(1,len(intervals)):
            if intervals[index][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[index][1])
            else:
                output.append(intervals[index])
        return output