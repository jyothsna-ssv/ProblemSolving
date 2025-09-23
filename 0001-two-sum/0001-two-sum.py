class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {} 

        for i, value in enumerate(nums):
            complement = target - value
            if complement in index_map:
                return [index_map[complement], i]
            index_map[value] = i