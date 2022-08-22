#https://leetcode.com/problems/maximum-gap/

import sys
maxSize = sys.maxsize
minSize = -sys.maxsize - 1
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2: return 0
        
        minnum=min(nums)
        maxnum=max(nums)
        # if the elements are same , then max gap will be zero (max and min will be same.)
        if maxnum==minnum:return 0
        
        gap=int((maxnum-minnum)/(n-1))
        if (maxnum-minnum)%(n-1)!=0:
            gap+=1
        print("gap : ",gap)
        min_bucket=[maxSize for _ in range(n)]
        max_bucket=[minSize for _ in range(n)]
        for i in range(n):
            bkt_number=int((nums[i]-minnum)//gap)
            min_bucket[bkt_number]=min(min_bucket[bkt_number],nums[i])
            max_bucket[bkt_number]=max(max_bucket[bkt_number],nums[i])
        print(min_bucket, max_bucket)
        prev=max_bucket[0]
        ans=0
        for i in range(n):
            if min_bucket[i]==maxSize:
                continue
            else:
                ans=max(ans,min_bucket[i]-prev)
                prev=max_bucket[i]
        return ans
