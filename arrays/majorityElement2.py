#https://leetcode.com/problems/majority-element-ii/
import sys
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count1=0
        count2=0
        first=sys.maxsize
        second=sys.maxsize
        for i in range(n):
            if first==nums[i]:
                count1+=1
            elif second==nums[i]:
                count2+=1
            elif count1==0:
                first=nums[i]
                count1=1
            elif count2==0:
                second=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in range(n):
            if nums[i]==first:
                count1+=1
            if nums[i]==second:
                count2+=1
        out=[]
        if count1>n//3:
            out.append(first)
        if count2>n//3:
            out.append(second)
        return out
