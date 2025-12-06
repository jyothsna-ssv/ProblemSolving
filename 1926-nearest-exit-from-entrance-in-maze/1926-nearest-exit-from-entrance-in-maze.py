class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque

        m,n = len(maze), len(maze[0])
        q=deque([(entrance[0],entrance[1],0)])
        visited=set([(entrance[0],entrance[1])])

        dirs=[(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r,c,d=q.popleft()

            for dr,dc in dirs:
                nr,nc = r+ dr, c+dc

                if 0<=nr < m and 0 <= nc < n and maze[nr][nc] == '.' and (nr,nc) not in visited:
                    if (nr == 0 or nr == m-1 or nc ==0 or nc == n-1) and [nr,nc] != entrance:
                        return d+1
                    visited.add((nr,nc))
                    q.append((nr, nc, d+1))
        return -1

        