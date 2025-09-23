class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # make sets to automatically remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # find elements unique to each set
        only_in_first = list(set1 - set2)
        only_in_second = list(set2 - set1)

        return [only_in_first, only_in_second]