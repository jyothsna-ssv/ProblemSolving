class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def dfs(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return 
            for num in range(start, 10):
                if total + num > n:
                    break
                dfs(num+1, path + [num], total+num)
        dfs(1,[],0)
        return res