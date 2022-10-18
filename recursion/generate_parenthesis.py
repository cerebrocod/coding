class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        s=['']*2*n
        l,r,i=0,0,0
        def pp(n,l,r,i,s):
            if i==2*n:
                ans.append(''.join(x for x in s))
                return
            if l==r:
                s[i]='('
                pp(n,l+1,r,i+1,s)
            elif l>r:
                if l==n:
                    s[i]=')'
                    pp(n,l,r+1,i+1,s)
                else:
                    s[i]='('
                    pp(n,l+1,r,i+1,s)
                    s[i]=')'
                    pp(n,l,r+1,i+1,s)
        pp(n,l,r,i,s)
        return ans
