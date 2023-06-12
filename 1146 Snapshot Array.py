class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        self.data = [[[0,0]] for _ in range(length)]
        self.updated = dict()
        self.snapID = -1

    def set(self, index: int, val: int) -> None:
        self.updated[index] = val

    def snap(self) -> int:
        self.snapID += 1
        for i, v in self.updated.items():
            if v != self.data[i][-1][1]: # it has changed
                self.data[i].append([self.snapID, v])
        self.updated = dict()
        return(self.snapID)

    def get(self, index: int, snap_id: int) -> int:
        arr = self.data[index]
        l = -1
        r = len(arr)
        while l+1 < r:
            mid = (l+r) // 2
            if arr[mid][0] <= snap_id:
                l = mid
            else:
                r = mid
        return arr[l][1]
