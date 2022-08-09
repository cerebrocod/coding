#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create split between two transactions
        # call it prefix profit array and suffix profit array
        n=len(prices)
        prefixmin=[0]*n
        prefixProfit=[0]*n
        
        prefixmin[0]=prices[0]
        for i in range(1,n):
            prefixmin[i]=min(prefixmin[i-1],prices[i])

        # prefix profit array
        prefixProfit[0]=0        
        for i in range(1,n):
            preprofit=prices[i]-prefixmin[i-1]
            prefixProfit[i]=max(prefixProfit[i-1],preprofit)

        # Similarly create suffix max and suffix profit array
        suffixmax=[0]*n
        suffixProfit=[0]*n
        
        suffixmax[n-1]=prices[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i]=max(suffixmax[i+1],prices[i])

        suffixProfit[n-1]=0
        for i in range(n-2,-1,-1):
            sufprofit=suffixmax[i+1]-prices[i]
            suffixProfit[i]=max(suffixProfit[i+1],sufprofit)

        ans=suffixProfit[0]
        for i in range(1,n):
            ans=max(ans,prefixProfit[i]+suffixProfit[i])
        
        return ans


