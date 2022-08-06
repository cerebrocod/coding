#https://leetcode.com/problems/rotate-array/

from typing import List

def reverse(nums:List[int],n:int) -> List[int]:
    i=0
    while(i<n//2):
        temp=nums[n-i-1]
        nums[n-i-1]=nums[i]
        nums[i]=temp
        i=i+1
    return nums

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        nums=reverse(nums,n)
        nums=reverse(nums,k)
        i=k
        while i<=(n+k-1)//2:
            temp=nums[n-i-1+k]
            nums[n-i-1+k]=nums[i]
            nums[i]=temp
            i=i+1
        return nums
