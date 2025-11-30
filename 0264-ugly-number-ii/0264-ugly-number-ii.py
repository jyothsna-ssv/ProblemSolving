class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen={1}
        for _ in range(n):
            val=heapq.heappop(heap)
            for mul in [2,3,5]:
                nxt=val*mul
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap,nxt)
        return val