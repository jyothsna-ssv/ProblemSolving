class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        left_heap=[]
        right_heap=[]

        i=0
        j=n-1

        for _ in range(candidates):
            if i<=j:
                heapq.heappush(left_heap, (costs[i], i))
                i+=1
        for _ in range(candidates):
            if i<=j:
                heapq.heappush(right_heap,(costs[j], j))
                j -= 1
        total=0

        # k workers

        for _ in range(k):
            pick_left=False

            if not right_heap:
                pick_left=True
            elif not left_heap:
                pick_left=False
            else:

                pick_left=left_heap[0]<=right_heap[0]
            if pick_left:
                cost, index =heapq.heappop(left_heap)
                total += cost

                if i<= j:
                    heapq.heappush(left_heap, (costs[i], i)) 
                    i +=1
            else:
                cost, index =heapq.heappop(right_heap)
                total += cost

                if i<= j:
                    heapq.heappush(right_heap, (costs[j], j)) 
                    j -=1
        return total   
