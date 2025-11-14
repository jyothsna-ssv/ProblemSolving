class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n+1)]

        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = diff[i][j]
                if i>0:
                    res[i][j] += res[i-1][j]
                if j>0:
                    res[i][j] += res[i][j-1]
                if i>0 and j>0:
                    res[i][j] -= res[i-1][j-1]
        return res
        