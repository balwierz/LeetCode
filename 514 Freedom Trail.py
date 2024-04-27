class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        states = [(0,0)]  # position, sum
        letter2pos = defaultdict(list)
        for pos, letter in enumerate(ring):
            letter2pos[letter].append(pos)
        for letter in key:
            newStates = []
            for pos in letter2pos[letter]:
                bestLen = inf
                for prevPos, prevLen in states:
                    dist = abs(pos - prevPos)
                    dist = min(dist, m-dist)
                    bestLen = min(bestLen, prevLen + dist)
                newStates.append([pos, bestLen])
            thr = min(thisLen for thisPos, thisLen in newStates) + m//2
            states = [state for state in newStates if state[1] <= thr]
            #states = newStates
        return len(key) + min(thisLen for thisPos, thisLen in states)
