import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)

        min_heap=[(matrix[0][0],0,0)]
        visited= set((0,0))

        while k > 0:
            val,r,c = heapq.heappop(min_heap)
            k -= 1

            if k == 0:
                return val
            if r+1 < n and (r+1,c) not in visited:
                heapq.heappush(min_heap, (matrix[r+1][c],r+1,c))
                visited.add((r+1,c))
            if c+1 < n and (r, c+1) not in visited:
                heapq.heappush(min_heap,(matrix[r][c+1],r,c+1))
                visited.add((r,c+1))
        