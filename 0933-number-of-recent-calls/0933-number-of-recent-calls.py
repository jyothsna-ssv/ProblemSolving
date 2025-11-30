from collections import deque
class RecentCounter:

    def __init__(self):
        self.q=deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        limit=t-3000

        while self.q[0] < limit:
            self.q.popleft()
        return len(self.q)
        


