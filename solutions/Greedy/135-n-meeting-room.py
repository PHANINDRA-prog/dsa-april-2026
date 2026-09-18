import heapq
class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        
        meeting_rooms = sorted(zip(start,end))
        
        heap = []
        
        heap.append(meeting_rooms[0][1])
        
        for i in range(1,len(meeting_rooms)):
            
            current_start_time , current_end_time = meeting_rooms[i]
            
            if current_start_time >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,current_end_time)
        return len(heap)