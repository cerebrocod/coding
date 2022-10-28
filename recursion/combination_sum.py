class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
        def comb(l,candidates,target,temp):
            if target==0:
                ans.append(temp.copy())
                return
            for i in range(l,len(candidates)):
                if candidates[i]<=target:
                    temp.append(candidates[i])
                    comb(i,candidates,target-candidates[i],temp)
                    temp.pop()
        comb(0,candidates,target,temp)        
        return ans
