#https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Transpose and reverse each row

        n=len(matrix)

        for i in range(n):
            for j in range(i):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        for i in range(n):
            for j in range(n//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-j-1]
                matrix[i][n-j-1]=temp

