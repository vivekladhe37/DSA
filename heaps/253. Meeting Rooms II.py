import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heapify(rooms)
        
        for i in range(len(intervals)):
            flag = False
            start = intervals[i][0]
            end = intervals[i][1]
            
            if not rooms:
                heapq.heappush(rooms,end)
            else:
                if rooms[0] <= start:
                    heapq.heappop(rooms)
                    heapq.heappush(rooms,end)
                else:
                    heapq.heappush(rooms,end)
                
        return len(rooms)