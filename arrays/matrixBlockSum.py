#https://leetcode.com/problems/matrix-block-sum/
#Idea: When the query is for cell (i, j), you actually look for cell (i + k, j + k) i.e. 
#the bottom right corner of the required block. The rest of the question is same as Range Sum Query 
#2D - Immutable.
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
	m=len(mat)
	n=len(mat[0])
        for i in range(m):
            sum_=0
            for j in range(n):
                sum_+=mat[i][j]
                mat[i][j]=_sum
        for j in range(n):
            sum_=0
            for i in range(m):
                sum_+=mat[i][j]
                mat[i][j]=_sum
        ans_mat=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                ii=min(i+k,m-1)
                jj=min(j+k,n-1)
                ans=mat[ii][jj]
                if i-k-1>=0:
                    ans-=mat[i-k-1][jj]
                if j-k-1>=0:
                    ans-=mat[ii][j-k-1]
                if i-k-1>=0 and j-k-1>=0:
                    ans+=mat[i-k-1][j-k-1]
                ans_mat[i][j]=ans
        return ans_mat
