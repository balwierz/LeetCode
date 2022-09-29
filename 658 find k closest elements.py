class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        i = bisect_left(arr, x) - 1
        #print("bisect = " + str(i))
        j = i+1
        nFound = 0
        while nFound < k:
            left = -9999999
            right = 999999
            if i >= 0:
                left = arr[i]
            if j < n:
                right = arr[j]
            if abs(x-left) <= abs(x - right):
                i -= 1
            else:
                j += 1
            nFound += 1
        return arr[i+1:j]
