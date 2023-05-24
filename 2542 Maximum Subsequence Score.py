class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        data = [(nums1[i], nums2[i]) for i in range(n)]
        if k == 1:
            return max(data[i][0] * data[i][1] for i in range(n))
        data.sort(reverse=True, key=lambda x: x[1])
        heap = [data[i][0] for i in range(k-1)]
        sum1 = sum(heap)
        heapify(heap)
        ret = 0
        for i in range(k-1, n):
            this = (sum1 + data[i][0]) * data[i][1]
            ret = max(ret, this)
            if data[i][0] > heap[0]:
                sum1 -= heappop(heap)
                heappush(heap, data[i][0])
                sum1 += data[i][0]
        return ret
