#https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''We go boundary by boundary and move inwards. That is the essential operation. First row, last column, last row, first column and then we move inwards by 1 and then repeat. That's all, that is all the simulation that we need.'''
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m
        top=0
        bottom=n
        result=[]
        while left<right and top<bottom:
            #left to right
            for index in range(left,right):
                result.append(matrix[top][index])
            top+=1

            #top to bottom
            for index in range(top,bottom):
                result.append(matrix[index][right-1])
            right-=1
            if not (left < right and top < bottom):
                break

            #right to left
            for index in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][index])
            bottom-=1

            #bottom to top
            for index in range(bottom-1,top-1,-1):
                result.append(matrix[index][left])
            left+=1

        return result
