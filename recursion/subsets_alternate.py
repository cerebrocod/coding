class Solution:
    def subsets(self,nums:List[int]):
       global_ans=[]
       def pas(tmp:List,nums:List,i:int,sz:int):
         if i==len(nums):
            global_ans.append([x for x in tmp if x!=-11])
            return
         tmp[sz]=nums[i]
         pas(tmp,nums,i+1,sz+1)
         tmp[sz]=-11
         pas(tmp,nums,i+1,sz) 
        
       tmp=[-11]*len(nums)
       pas(tmp,nums,0,0)
       return global_ans
