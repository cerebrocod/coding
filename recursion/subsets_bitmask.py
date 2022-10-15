from typing import List
class Solution:
    def subsets(self,nums:List[int]):
        n=len(nums)
        ans=[]
        for i in range(2**n):
            sub=[-11 for _ in range(n)]
            mask=format(i,'0'+str(n)+'b')
            print(mask)
            sub=[x for j,x in enumerate(nums) if int(mask[j])]
            ans.append(sub)
        return ans


