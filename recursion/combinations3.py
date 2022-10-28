class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp=[0 for _ in range(k)]
        N=n
        ans=[]
        def combinations(temp,ans,i,sz,n):
            if n<0: return
            if i==k:
                ans.append(temp.copy())
                return
            temp[sz]=n
            combinations(temp,ans,i+1,sz+1,n-1)
            combinations(temp,ans,i,sz,n-1)
                        
        combinations(temp,ans,0,0,9)
        ans=[an for an in ans if sum(an)==N]
        print(ans)
        return ans
