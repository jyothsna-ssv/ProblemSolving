class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque()
        D=deque()
        n=len(senate)

        for i, ch in enumerate(senate):
            (R if ch == 'R' else D).append(i)
        while R and D:
            r=R.popleft()
            d=D.popleft()
            if r<d:
                R.append(r+n)
            else:
                D.append(d+n)
        return "Radiant" if R else "Dire"