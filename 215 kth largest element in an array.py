def partition(arr, left, right):
    '''returns an index of a pivot
    indices are inclusive [, ]'''
    #print("call: " + str(left) + " " + str(right))
    pivotI = (left+right) // 2
    arr[right], arr[pivotI] = arr[pivotI], arr[right]
    pivot = arr[right]
    #print("  pivot " + str(pivot))
    p = left
    for i in range(left, right):  # excluding right
        if arr[i] > pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    arr[right], arr[p] = arr[p], arr[right]
    #print("returning: " + str(p) + " " + ','.join([str(i) for i in arr]))
    return p

def findKth(arr, k, left, right):
    '''k-which highest number to find'''
    while left < right:
        w = partition(arr, left, right)
        if w == k:
            return arr[w]
        if k < w:
            right = w-1
        else:
            left = w+1
    return arr[left]
    
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return findKth(nums, k-1, 0, len(nums)-1)
        #return sorted(nums)[-k]
