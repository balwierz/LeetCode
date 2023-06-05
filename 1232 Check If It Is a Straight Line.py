import numpy as np
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = np.array(coordinates)
        means = np.mean(a, 0)   
        v0, v1 = np.linalg.svd(a - means, compute_uv=False)
        return abs(v1) < 1e-10
