class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        n=len(s)
        path=[]
        def backtrack(start,path):
            if len(path)==4 and start==n:
                ans.append(".".join(path[:]))
                print(path)
                return
            for i in range(start+1,min(start+4,len(s)+1)):
                sub=s[start:i]
                
                if not 0<=int(sub)<=255:
                    continue
                if not sub=='0' and not sub.lstrip("0")==sub:
                    continue
                path.append(sub)
                backtrack(i,path)
                path.pop()
        backtrack(0,path)
        print(ans)
        return ans
