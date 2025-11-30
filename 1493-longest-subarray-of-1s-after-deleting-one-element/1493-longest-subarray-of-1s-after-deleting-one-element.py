class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeroes=0
        ans=0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans-1