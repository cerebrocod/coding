class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp=[0 for _ in range(k)]
        ans=[]
        def combinations(temp,ans,i,sz,n):
            if n<0: return
            if i==k:
                ans.append(temp.copy())
                print(temp)
                return
            temp[sz]=n
            combinations(temp,ans,i+1,sz+1,n-1)
            combinations(temp,ans,i,sz,n-1)
                        
        combinations(temp,ans,0,0,n)
        return ans
