class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        best=curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            best = max(best, curr)
        return best / k