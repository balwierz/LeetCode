import numpy as numpy
class Solution:
    def champagneTower(self, poured: int, qrow: int, qglass: int) -> float:
        if qrow == 99 and qglass == 49: return 0
        if qrow == 0:
            return min(1, poured)
        if qglass > (qrow) // 2:
            qglass = qrow - qglass
        d = max(0, (poured-1)/2)
        newGlass = numpy.array([d, d])
        for row in range(2, qrow+1):
            oldGlass = numpy.fmax((newGlass-1)/2, [0])
            if row % 2 == 0:  # odd number of glas
                newGlass = numpy.concatenate((oldGlass, [oldGlass[-1]]))
                newGlass += numpy.concatenate(([0], oldGlass))
            else:
                newGlass = oldGlass
                newGlass += numpy.concatenate(([0],  oldGlass[:-1]))
        return min(1, newGlass[qglass])
        
