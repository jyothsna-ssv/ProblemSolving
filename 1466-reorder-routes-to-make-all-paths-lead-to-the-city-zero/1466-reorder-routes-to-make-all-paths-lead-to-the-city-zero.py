
# treat all roads as undirected but mark original directions.
# DFS starts from 0 every time you traverse an edge originally pointing away from you, count one reversal
# Sum of such edges is the minimum chages needed.
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]

        for a,b in connections:
            g[a].append((b,1))
            g[b].append((a,0))
        visited=set()

        def dfs(city):
            visited.add(city)
            changes=0

            for nbr,cost in g[city]:
                if nbr not in visited:
                    changes += cost + dfs(nbr)
            return changes
        return dfs(0)
        