class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        x = (nums[:],k)
        uniques=set(nums)
        sorted_dist_desc= sorted(uniques, reverse=True)
        return sorted_dist_desc[:k]