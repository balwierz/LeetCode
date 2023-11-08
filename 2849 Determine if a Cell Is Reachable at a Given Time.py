def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    d = max(abs(fx-sx), abs(fy-sy))
    return d <= t and (d != 0 or t != 1)        
