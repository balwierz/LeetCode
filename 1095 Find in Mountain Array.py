def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
    @cache
    def get(i):
        return arr.get(i)
    
    n = arr.length()
    if target < min(get(0), get(n-1)):
        return -1
    
    top = bisect_left(list(range(n-1)), True, key=lambda i: get(i) > get(i+1))
    if target > get(top):
        return -1

    if get(0) <= target:
        left = bisect_left(list(range(top)), True, key=lambda i: target <= get(i))
        if target == get(left):
            return left
    
    right = bisect_left(list(range(top, n)), True, key=lambda i: target >= get(i)) + top
    if target == get(right):
        return right
    
    return -1
