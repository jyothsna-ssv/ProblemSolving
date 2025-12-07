
# i>>1 removes last bit
# (i&1) checks if the last bit is 1
# bits(i) = bits(i//2) + last_bit
# dp 0 to n
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0] * (n+1)
        for i in range(1, n+1):
            dp[i]=dp[i>>1]+(i&1)
        return dp