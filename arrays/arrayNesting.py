#https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # determine the largest cycle
        ans=0
        n=len(nums)
        if n==1: return 1
        for i in range(n):
            if nums[i]>0:
                #count of each cycle measured in count
                ind,val,count=nums[i],i,0
                #cycles here
                while ind!=i:
                    count+=1
                    temp=nums[ind]
                    nums[ind]=-(val+1)
                    val=ind
                    ind=temp
    #since last value is not taken into account in the ealier loop
                nums[ind]=-(val+1)
                ans=max(ans,count+1)
        return ans
