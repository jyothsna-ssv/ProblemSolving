# each eq a/b = v forms edges a->b(v) and b->a(1/v)
# DFS from N -> D, mutliplying edge weights along the path.
# if a path exists, return the prod , otherwise return -1.0.


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g={}

        for (a,b), v in zip(equations, values):
            g.setdefault(a, []).append((b, v))
            g.setdefault(b, []).append((a, 1/v))
        
        def dfs(curr, target, visited, acc):
            if curr == target:
                return acc
            visited.add(curr)
            for nbr, val in g.get(curr, []):
                if nbr not in visited:
                    res = dfs(nbr, target, visited, acc*val)
                    if res != -1.0:
                        return res
            return -1.0
        ans=[]

        for a,b in queries:
            if a not in g or b not in g:
                ans.append(-1.0)
            else:
                ans.append(dfs(a,b,set(),1.0))
        return ans
        