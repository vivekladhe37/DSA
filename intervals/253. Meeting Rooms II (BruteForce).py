class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        rooms = []
        
        for i in range(len(intervals)):
            flag = False
            start = intervals[i][0]
            end = intervals[i][1]
            
            if not rooms:
                rooms.append(end)
            else:
                for j in range(len(rooms)):
                    if rooms[j] <= start:
                        rooms[j] = end
                        flag = True
                        break
                if flag == False:
                    rooms.append(end)
        
        return len(rooms)