#https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self,matrix:List[List[int]],target:int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        i=0
        j=m-1
        while i<n and j>=0:
            if matrix[i][j]==target: return True
            if matrix[i][j]<target:
                i=i+1 
            else:
                j=j-1
        return False

