class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #loop through every city
        #if not visited -> starts a new province
        #DFS marks all cities connected to it
        #Increment province count

        n=len(isConnected)
        visited = set()

        def dfs(city):
            for nbr in range(n):
                if isConnected[city][nbr] == 1 and nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr)
        provinces = 0

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1
        return provinces
        