#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results=[]
        if numRows==1:
            results.append([1])
        elif numRows==2:
            results.append([1])
            results.append([1,1])
        else:
            results.append([1])
            results.append([1,1])
            for i in range(2,numRows):
                res=[1]
                for j in range(1,i):
                    print(i,j,results)
                    res.append(results[i-1][j]+results[i-1][j-1])
                res.append(1)
                results.append(res)
        return results


