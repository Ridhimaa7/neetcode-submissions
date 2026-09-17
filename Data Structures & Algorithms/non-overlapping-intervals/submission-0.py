class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        current_start, current_end = intervals[0]
        reslist = [[current_start, current_end]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= current_end:
                reslist.append(intervals[i])
                current_end = intervals[i][1]
        return len(intervals) - len(reslist)