class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        c = Counter(senate)
        nR = c["R"]  # num remaining
        nD = c["D"]
        nCancelR, nCancelD = 0, 0
        q = deque(senate)
        while nR and nD:
            e = q.popleft()
            if e == "R":
                if nCancelR:
                    nCancelR -= 1
                    continue
                nCancelD += 1
                nD -= 1
                q.append(e)
            else: # D
                if nCancelD:
                    nCancelD -= 1
                    continue
                nCancelR += 1
                nR -= 1
                q.append(e)
        return "Dire" if nD else "Radiant"
