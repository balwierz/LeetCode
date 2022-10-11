import numpy as np

# various ways of inverting a permutation. Best guess that the last one is the fastest.
def invert_permutation_list_scan(p):
    return [p.index(l) for l in range(len(p))]

def invert_permutation_list_comp(permutation):
    return [i for i, j in sorted(enumerate(permutation), key=lambda i_j: i_j[1])]

def invert_permutation_numpy(permutation):
    return np.argsort(permutation)

def invert_permutation_numpy2(permutation):
    inv = np.empty_like(permutation)
    inv[permutation] = np.arange(len(inv), dtype=inv.dtype)
    return inv

# A class defining Binary Indexed Tree:
class BIT:
    def __init__(self, maxN):
        self.maxN = maxN
        self.bit = [0] * maxN
    def prefSum(self, n):
        ''' return prefix sum'''
        ret = 0
        while n > 0:
            ret += self.bit[n]
            n -= n & (-n)
        return ret
    def insert(self, v, delta):
        while v < self.maxN:
            self.bit[v] += delta
            v += v & (-v)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
		# We have 3 permutations. The central one is the identity P_0 = [0, ..., n-1]. P_1 = nums1
		# and P_2 = nums2 are remaining two permutations. Reverting the second permutation 
		# and chaining it with the first permutation P_1 * P^{-1}_0 = P'is the permutation we should
		# study. We are asking how many triples (i, j, k indices) with growing values P' has.
        perm = invert_permutation_numpy2(nums2)[np.array(nums1)]
        ret = 0 # return value
        a = BIT(int(1e5+1))  # a BIT for 1-digit subsequences, storing their end values
        b = BIT(int(1e5+1))  # a Bit for 2-digit subsequences, storing values of second digits
        for v in perm:
			# finish 2-digit subsequences with this (v) last digit
            ret += b.prefSum(v)
			# count how many 1-digit subsequences it extends to two digit, v being the second digit
            cnt = a.prefSum(v)
			# update 2-digit number, v+1 because BIT stores only positive numbers. 
			# Above v is also a short way of saying (v - 1) + 1, because the previous digit must be lower.
            b.insert(v+1, cnt)
			# update 1-digit number by inserting v in copy number 1.
            a.insert(v+1, 1)
        return ret
