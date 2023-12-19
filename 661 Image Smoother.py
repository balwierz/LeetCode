class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        mat1 = [[0] * n for _ in range(m)]
        if n >= 2:
            for rowI, row in enumerate(img):
                s = row[0] + row[1]
                mat1[rowI][0] = s
                for colI in range(1, n-1):
                    s += row[colI+1]
                    if colI >= 2:
                        s -= row[colI-2]
                    mat1[rowI][colI] = s
                mat1[rowI][n-1] = row[n-2] + row[n-1]
        else:  # n == 1:
            mat1 = copy.deepcopy(img)
        print(mat1)
        for colI in range(n):
            if m >= 2:
                s = mat1[0][colI] + mat1[1][colI]
                img[0][colI] = s // ((4 if n>1 else 2) if colI==0 or colI == n-1 else 6)
                for rowI in range(1, m-1):
                    s += mat1[rowI+1][colI]
                    if rowI >= 2:
                        s -= mat1[rowI-2][colI]
                    img[rowI][colI] = s // ((6 if n>1 else 3) if colI==0 or colI == n-1 else 9)
                # last row
                img[m-1][colI] = (mat1[m-1][colI] + mat1[m-2][colI]) // ((4 if n>1 else 2) if colI==0 or colI==n-1 else 6)
            else: # m == 1
                if n == 1:
                    pass
                else:
                    img[0][colI] = mat1[0][colI] // (2 if colI == 0 or colI == n-1 else 3)
        return img

from itertools import product
import numpy as np 
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        img_np = np.zeros((m+2, n+2), dtype=np.int32)
        img_np[1:-1, 1:-1] = img
        cnt_np = np.zeros((m+2, n+2), dtype=np.int32)
        cnt_np[1:-1, 1:-1] = 1

        reduce_img = lambda x: sum([x[o1:m+o1, o2:n+o2] for o1, o2 in product(range(3), range(3))])


        ans = reduce_img(img_np) // reduce_img(cnt_np)
        return ans.tolist()
