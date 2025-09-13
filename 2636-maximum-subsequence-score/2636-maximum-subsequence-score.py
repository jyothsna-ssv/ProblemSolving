class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1)
        order=sorted(range(n), key=lambda i: nums2[i], reverse=True)
        min_heap=[]
        curr_sum=0
        best=0

        for i in order:
            m=nums2[i]
            a=nums1[i]

            heapq.heappush(min_heap,a)
            curr_sum +=a

            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)

            if len(min_heap)==k:
                best=max(best, curr_sum *m)
        return best