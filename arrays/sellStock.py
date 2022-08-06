#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prefixmin=[0]*n
        suffixmax=[0]*n
        prefixmin[0]=prices[0]
        suffixmax[n-1]=prices[n-1]
        for i in range(1,n):
            prefixmin[i]=min(prefixmin[i-1],prices[i])
        for i in range(n-2,-1,-1):
            suffixmax[i]=max(suffixmax[i+1],prices[i])
        ans=0
        for i in range(n):
            ans=max(ans,suffixmax[i]-prefixmin[i])
        return ans
