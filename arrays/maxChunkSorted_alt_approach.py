
#https://leetcode.com/problems/max-chunks-to-make-sorted
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
	n=len(arr)
	prefixmax=[0]*n
	prefixmax[0]=arr[0]
	for i in range(1,n):
	   prefixmax[i]=max(prefixmax[i-1],arr[i])
        ans=0
	for i in range(n):
	   if prefixmax[i]==i:
		ans+=1
        return ans
