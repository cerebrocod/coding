#://leetcode.com/problems/max-chunks-to-make-sorted/
def chunked(arr,i,j):
    count=0
    k=i
    while k>=i and k<=j:
        if arr[k]>=i and arr[k]<=j:
            count+=1
        k+=1
    if count==j-i+1:
        return True
    else:
        return False
    
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0;i=0
        while i<n:
            j=i
            while j<n:
                if chunked(arr,i,j):
                    break
                j+=1    
            i=j+1
            ans=ans+1

        return ans
