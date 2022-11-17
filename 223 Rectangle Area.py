def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        uArea = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        iArea = max(- max(ax1, bx1) + min(ax2, bx2), 0 ) * \
            max(- max(ay1, by1) + min(ay2, by2), 0)
        return uArea - iArea
