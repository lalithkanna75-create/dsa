class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l=0
        r=len(mat[0])-1

        while l<=r:
            m=(l+r)//2

            maxrow=0

            for i in range(len(mat)):
                if mat[i][m]>mat[maxrow][m]:
                    maxrow=i

            if m>0 and mat[maxrow][m-1]>mat[maxrow][m]:
                r=m-1

            elif m<len(mat[0])-1 and mat[maxrow][m+1]>mat[maxrow][m]:
                l=m+1

            else:
                return [maxrow,m]