class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x:x[0])
        resarr = []

        for i in range(len(intervals)):
            if not resarr:
                resarr.append(intervals[i])
            else:
                if intervals[i][0] <= resarr[-1][1]:
                    resarr[-1][1] = max(intervals[i][1], resarr[-1][1])
                else:
                    resarr.append(intervals[i])
        
        return resarr
