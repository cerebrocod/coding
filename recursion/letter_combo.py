digitMap={2:['a','b','c'],
          3:['d','e','f'],
          4:['g','h','i'],
          5:['j','k','l'],
          6:['m','n','o'],
          7:['p','q','r','s'],
          8:['t','u','v'],
          9:['w','x','y','z']}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        if len(digits)==0:
            return []
        def lc(digits,i,tmp):
            if i==len(digits):
                ans.append(tmp)
                return
            for k in range(len(digitMap[int(digits[i])])):
                lc(digits,i+1,tmp+digitMap[int(digits[i])][k])
        lc(digits,0,'')
        return ans
