class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c = Counter(moves)
        return abs(c['L']-c['R']) + c['_']
