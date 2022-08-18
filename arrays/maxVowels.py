#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
#Input: s = "abciiidef", k = 3
#Output: 3
#Explanation: The substring "iii" contains 3 vowel letters
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        count_vowels=0
        for i in range(k):
            if s[i] in 'aeiou':
                count_vowels+=1
        ans = count_vowels
        for j in range(k,n):
            if s[j] in 'aeiou':
                count_vowels+=1
            if s[j-k] in 'aeiou':
                count_vowels-=1
            ans=max(ans,count_vowels)
        return ans

	
