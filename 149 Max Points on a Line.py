mil = 1000000
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def abc(u, v):
            if v[0] - u[0] == 0:
                return (0, u[0])
            a = (u[1] - v[1]) / (v[0]-u[0])
            norm = sqrt(a*a + 1) #abs(a) + 1   # taxi metrics
            a /= norm
            b = 1/norm
            c = 0.5*(a*(u[0]+v[0]) + b*(u[1]+v[1]))
            return (int(mil*b), int(mil*c))
        lines = defaultdict(int)
        ret = 0
        n = len(points)
        for v in range(1, n):
            for u in range(v):
                thisAbc = abc(points[u], points[v])   # a tuple
                print(u, " ", v, " ", lines[thisAbc]+1, " ", thisAbc)
                lines[thisAbc] += 1
                ret = max(ret, lines[thisAbc])
        return int(0.5 + 0.5 * sqrt(1 + 8*ret))
