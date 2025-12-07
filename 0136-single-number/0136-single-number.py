# XOR : a^a=0, a^0=a


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for n in nums:
            x ^=n
        return x