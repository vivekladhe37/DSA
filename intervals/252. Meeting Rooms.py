class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort(key = lambda x:x[0])
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if start < intervals[i-1][1]:
                return False
        
        return True