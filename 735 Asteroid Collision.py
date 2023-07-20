class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        left = []
        for a in asteroids:
            if a > 0:
                left.append(a)
            else: # a <0
                equally = False
                while len(left) and left[-1] + a <= 0:
                    if a + left[-1] == 0:
                        equally = True
                    left.pop()
                    if equally:
                        break
                if not len(left) and not equally:
                    ret.append(a)
        ret.extend(left)
        return ret
