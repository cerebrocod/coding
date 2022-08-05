# Use precomputation approach to calculate
    #1.prefix max
    #2.suffix max
    #3 rainwater clogged at a particular tower
    #  min(prefixmax[i],suffixmax[i])-height[i]

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefixmax=[0]*n
        suffixmax=[0]*n
        #calculate prefix max
        maxm=height[0]
        for i in range(n):
            if maxm<height[i]:
                maxm=height[i]
                prefixmax[i]=maxm
            else:
                prefixmax[i]=maxm
        
        #calculate suffix max
        maxm=height[n-1]
        for i in range(n-1,0,-1):
            if maxm<height[i]:
                maxm=height[i]
                suffixmax[i]=maxm
            else:
                suffixmax[i]=maxm

        ans=0
        for i in range(n):
            ans+=min(0,min(suffixmax[i],prefixmax[i])-height[i])
        return ans


