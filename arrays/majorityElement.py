#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=-1
        votes=0
        n=len(nums)
        for i in range(n):
            if votes==0:
                candidate=nums[i]
                votes=1
            else:
                if nums[i]==candidate:
                    votes+=1
                else:
                    votes-=1
        return candidate
