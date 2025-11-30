class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq={}
        ops=0

        for x in nums:
            target = k-x

            if target in freq and freq[target] > 0:
                ops += 1
                freq[target] -= 1
            else:
                freq[x] = freq.get(x,0) + 1
        return ops