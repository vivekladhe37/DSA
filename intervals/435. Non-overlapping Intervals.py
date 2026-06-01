class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])
        res = 0
        acceptedEnd = intervals[0][1]

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if acceptedEnd > start:
                    res += 1
            else:
                acceptedEnd = end
        
        return res
