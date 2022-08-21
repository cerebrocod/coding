#https://leetcode.com/problems/permutation-in-string/
class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            n1=len(s1)
            n2=len(s2)
            if n2<n1: return False            
            freq_s1=[0]*26
            freq_s2=[0]*26
            for i in range(n1):
                freq_s1[ord(s1[i])-ord('a')]+=1
                freq_s2[ord(s2[i])-ord('a')]+=1
            if freq_s1==freq_s2: return True
            for i in range(n1,n2):
                freq_s2[ord(s2[i-n1])-ord('a')]-=1
                freq_s2[ord(s2[i])-ord('a')]+=1
                if freq_s1==freq_s2:
                    return True
            return  False
                
