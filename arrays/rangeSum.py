#https://leetcode.com/problems/range-sum-query-2d-immutable/submissions/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #prefix sum across rows followed by prefix sum across columns
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                if j>0:
                    matrix[i][j]+=matrix[i][j-1]
        for j in range(n):
            for i in range(1,m):
                if i>0:
                    matrix[i][j]+=matrix[i-1][j]
        self.matrix=matrix
        print(self.matrix)
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=self.matrix[row2][col2]
        if col1>0:
            ans-=self.matrix[row2][col1-1]
        if row1>0:
            ans-=self.matrix[row1-1][col2]
        if row1>0 and col1>0:
            ans+=self.matrix[row1-1][col1-1]
        return ans
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
