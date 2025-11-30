class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events=[]

        for L,R,H in buildings:
            events.append((L,-H,R))
            events.append((R,0,0))
        events.sort()

        heap=[(0,float('inf'))]
        res=[]

        for x, HH, R in events:
            if HH != 0:
                heapq.heappush(heap,(HH,R))
            
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            curr_height = -heap[0][0]

            if not res or res[-1][1] != curr_height:
                res.append([x,curr_height])
        return res