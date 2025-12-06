
# to reach step i, must come from i-1 or i-2
# trach only the last two dp states for minimal cost
# at the end, the top can be reached from either of the last two steps 
# return minimum

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)

        dp0, dp1 = 0,0

        for i in range(n):
            curr=min(dp0, dp1)+ cost[i]
            dp0, dp1=dp1,curr
        return min(dp0,dp1)
        