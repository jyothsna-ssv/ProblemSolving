# either rob this house add its money to dp[i-2]
# or skip if keep dp[i-1]
# track only two states rob1, rob2 and update iteratively
# final val in rob2 is the maximum amount you can rob without hitting adjacent houses.


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in nums:
            newRob = max(rob2, rob1+n)
            rob1, rob2 = rob2, newRob
        return rob2        