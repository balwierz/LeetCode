class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:     
        # find the bottom tree(s)
        bottom = set()
        b = 101
        for i in range(len(trees)):
            if trees[i][1] < b:
                b = trees[i][1]
                bottom = set()
            if trees[i][1] == b:
                bottom.add(i)
        isFence = set()
        maxx = -1
        for i in bottom:
            isFence.add(i)
            if trees[i][0] > maxx:
                maxx = trees[i][0]
                axis = i
        dir = [1, 0]  # start horizontally to the right
        while True:   # loop over axes / vertices of the hull
            #print("a: ", axis)
            thisEdge = set()
            bestCos = -2;
            norm = sqrt(dir[0]**2 + dir[1]**2)
            dir[0] /= norm   # normalise
            dir[1] /= norm   # normalise
            for i in range(len(trees)):
                #print(i)
                x = trees[i][0] - trees[axis][0]
                y = trees[i][1] - trees[axis][1]
                cos = dir[0] * x + dir[1] * y
                norm2 = sqrt(x*x + y*y)
                if norm2 == 0:
                    continue
                cos /= norm2
                if cos > bestCos + 0.00000000001:
                    bestCos = cos
                    thisEdge = set()
                if abs(cos - bestCos) < 0.00000000001:
                    thisEdge.add(i)
            newAxis = axis
            #print("thisEdge: ", thisEdge)
            bestDist = 0
            for i in thisEdge:
                isFence.add(i)
                dist = (trees[i][0] - trees[axis][0])**2 + (trees[i][1] - trees[axis][1])**2
                if dist > bestDist:
                    bestDist = dist
                    newAxis = i
            dir = [trees[newAxis][0] - trees[axis][0], trees[newAxis][1] - trees[axis][1]]
            axis = newAxis
            if axis in bottom:
                break
        return [trees[i] for i in isFence]
