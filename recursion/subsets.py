from typing import List
class Solution:
    def subsets(self,nums:List[int]):
        if nums==[]:
            return [[]]
        x=self.subsets(nums[1:])
        return x+[[nums[0]]+y for y in x]
         
