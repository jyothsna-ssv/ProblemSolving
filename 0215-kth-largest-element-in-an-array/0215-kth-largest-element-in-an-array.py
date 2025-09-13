class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for x in nums:
            if len(h)<k:
                heapq.heappush(h,x)
            elif x>h[0]:
                heapq.heappop(h)
                heapq.heappush(h,x)
        return h[0]

        