# each cell's ways = ways from top + ways from left
# use a 1D array to put these values row by row
# last cell holds the total no of unique paths.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n

        for _ in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]