class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def upheap(i):    # maxheap
            nonlocal n
            while i>1 and nums[i] > nums[i>>1]:
                nums[i], nums[i>>1] = nums[i>>1], nums[i]
                i = i>>1
        def downheap(i):
            nonlocal n
            while i<= n:
                toSwapI = i
                if i<<1 <= n:
                    if nums[i<<1] > nums[i]:
                        toSwapI = i<<1
                    if (i<<1) + 1 <= n:
                        if nums[(i<<1)+1] > nums[toSwapI]:
                            toSwapI = (i<<1)+1
                    if toSwapI != i:
                        nums[i], nums[toSwapI] = nums[toSwapI], nums[i]
                        i = toSwapI
                    else:
                        break
                else:
                    break
        def heapSort():
            nonlocal n
            nums.append(nums[0])
            for i in range(2, n+1):
                upheap(i)
            print(nums)
            for i in range(n, 1, -1):
                nums[1], nums[i] = nums[i], nums[1]
                n -= 1
                downheap(1)
                
        def qs(a, l, r):
            if l >= r: return
            p, i, j = a[l], l+1, r
            while True:
                while i < r and a[i] < p: i+=1
                while j >= l+1 and p < a[j]: j-=1
                if i>=j: break
                a[i], a[j] = a[j], a[i]
            a[l], a[j] = a[j], a[l]

            qs(a, l, j-1)
            qs(a, j+1, r)

        def qsort(a):
            if len(a) <=1: return a
            lt = [x for x in a if x < a[0]]
            eq = [x for x in a if x == a[0]]
            gt = [x for x in a if x > a[0]]
            return qsort(lt) + eq + qsort(gt)

        def ms(a):
            if len(a) <=1: return a
            i, j, n, res = 0, 0, len(a), []
            al = ms(a[:n//2])
            ar = ms(a[n//2:])
            while i < len(al) and j < len(ar):
                if al[i] < ar[j]: res.append(al[i]); i += 1
                else: res.append(ar[j]); j += 1
            if i < len(al): res.extend(al[i:])
            if j < len(ar): res.extend(ar[j:])
            return res

        def bs(a):
            n = len(a)
            for i in range(n-1):
                for j in range(1, n-i):
                    if a[j-1] > a[j]: a[j], a[j-1] = a[j-1], a[j]
            return a

        def ins(a):  # Build sorted array up to i
            n = len(a)
            for i in range(1, n):
                for j in range(i, 0, -1):
                    if a[j-1] > a[j]: a[j], a[j-1] = a[j-1], a[j]
            return a

        def ss(a):  # Move the min of the current subarray.
            for i in range(len(a)-1):
                idx = a[i:].index(min(a[i:]))
                a[i], a[idx+i] = a[idx+i], a[i]
            return a

        def hs(a):
            import queue
            q = queue.PriorityQueue()
            for i in a: q.put(i)
            res = [q.get() for _ in range(len(a))]
            return res

        def hs2(a):
            heapq.heapify(a)
            return [heapq.heappop(a) for _ in range(len(a))]

        def hs3(a):
            def heapify(a, n, i):
                l, r = 2*i+1, 2*i+2
                if l >= n: return
                s = r if r < n and a[r] < a[l] else l  # smaller
                if i != s and a[s] < a[i]:
                    a[i], a[s] = a[s], a[i]
                    heapify(a, n, s)
            n, res = len(a), []
            for i in range((n-1)//2, -1, -1):
                heapify(a, n, i)
            while True:
                res.append(a[0])
                last = a.pop()
                if a: a[0] = last
                else: break
                heapify(a, len(a), 0)
            return res
            
        def quicksort(a):
            def qs(a, l, r):
                if l >= r: return
                p, i, j = a[l], l+1, r
                while True:
                    while i<r and a[i]<p: i+=1
                    while j>l and a[j]>p: j-=1
                    if i>=j: break
                    a[i], a[j] = a[j], a[i]
                a[l], a[j] = a[j], a[l]
                qs(a, l, j-1)
                qs(a, j+1, r)
            random.shuffle(a)
            qs(a, 0, len(a)-1)
            return a

        def bubblesort(a):
            n = len(a)
            for i in range(n-1):
                for j in range(1, n-i):
                    if a[j] < a[j-1]: a[j], a[j-1] = a[j-1], a[j]
            return a

        def heapsort(a):
            def heapify(a, n, i):
                l, r, smaller = 2*i+1, 2*i+2, i
                if l >= n: return
                smaller = r if r < n and a[r] < a[l] else l
                if a[smaller] < a[i]:
                    a[i], a[smaller] = a[smaller], a[i]
                    heapify(a, n, smaller)              
            for i in range((len(a)-1)//2, -1, -1):
                heapify(a, len(a), i)
            res = []
            while True:
                res.append(a[i])
                last = a.pop()
                if not a: return res
                a[0] = last
                heapify(a, len(a), 0)
            return res

        def mergesort(a):
            if len(a) <= 1: return a
            m = len(a)//2
            al, ar, l, r, res = mergesort(a[:m]), mergesort(a[m:]), 0, 0, []
            while l < len(al) and r < len(ar):
                if al[l] < ar[r]: res.append(al[l]); l += 1
                else: res.append(ar[r]); r += 1
            if l < len(al): res.extend(al[l:])
            if r < len(ar): res.extend(ar[r:])
            return res

        def radixsort(a, base=10):
            n_digits = len(str(max(a)))
            for d in range(n_digits):
                res = [[] for _ in range(base)]
                for i in a: res[i // base**d % base].append(i)
                a = [x for y in res for x in y]
            return a

        def radixsort2(a, base=1000):
            def get_n(i):
                n = 1
                while abs(i) // base**n: n += 1
                return n
            n_digits = max(get_n(x) for x in a)
            for d in range(n_digits):
                res = {k: [] for k in range(-base+1, base)}
                for i in a:
                    k = abs(i) // base**d % base
                    res[-k if i < 0 else k].append(i)
                a = [x for k in res for x in res[k]]
            return a


        # random.shuffle(nums)
        # qs(nums, 0, len(nums)-1)
        # nums = qsort(nums)
        # nums = ms(nums)
        # nums = bs(nums)
        # nums = ins(nums)
        # nums = ss(nums)
        # nums = hs(nums)
        # nums = hs2(nums)
        # nums = hs3(nums)
        # return bubblesort(nums)
        # return mergesort(nums)
        # return radixsort(nums)
        return radixsort2(nums)
        # return nums

# class Solution:

    
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     # self.quickSort(nums)
    #     # self.mergeSort(nums)
    #     # self.bubbleSort(nums)
    #     # self.insertionSort(nums)
	# 	# self.selectionSort(nums)
    #     # self.heapSort(nums)
    #     # nums = self.qsort(nums)
    #     def partition(a, le, ge):
    #         # assumption: le < ge
    #         i = le + 1
    #         while i <= ge:
    #             if a[i] < a[le]:
    #                 a[i], a[le] = a[le], a[i]
    #                 i += 1; le += 1
    #             elif a[i] > a[le]:
    #                 a[i], a[ge] = a[ge], a[i]
    #                 ge -= 1
    #             else:
    #                 i += 1
    #         return le, ge
                    
    #     def quicksort(a, l, r):
    #         le, ge = partition(a, l, r)
    #         if l < le-1: quicksort(a, l, le-1)
    #         if ge+1 < r: quicksort(a, ge+1, r)
                
    #     n = len(nums)
    #     if n <= 1: return nums
                
    #     quicksort(nums, 0, n-1)
    #     return nums
        
    
	# @bubbleSort, TLE
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
	# @insertionSort, TLE
    def insertionSort(self, nums): 
        for i in range(1, len(nums)): 
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j] : 
                    nums[j + 1] = nums[j] 
                    j -= 1
            nums[j + 1] = key
		
	# @selectionSort, TLE
    def selectionSort(self, nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums
    
	# @quickSort
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums
     
	# @mergeSort
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
   
    def qsort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]
        return self.qsort(lt) + eq + self.qsort(gt)  

   # @heapSort
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 
