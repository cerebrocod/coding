#https://leetcode.com/problems/first-missing-positive/
#A problem requiring O(n) time and constant extra space, really hard!

#Use the original input list to work as a hashmap!
#We will let:
#mark the value of that index as negative <=> mark that index as visited

#I will explain step by step using an example:
#[3 4 -1 1]

###1. First, we should know that the first missing positive should be at most len(list) + 1,
##(for example, input list:[1 2 3 4], first missing positive is 5).

#2. In the first loop of the array list, we let number that are not in the range 1:n be n + 1.
#In the example:
#[3 4 -1 1] -> [3 4 5 1]
#
#3. In the second loop, for every number, if its original value is not equal to n + 1, make it opposite.
#In the example:
#[3 4 5 1]
#-> [3 4 -5 1] (integer 3 exists, value of index 2 negative)
#-> [3 4 -5 -1] (integer 4 exists, value of index 3 negative)
#-> [3 4 -5 -1] (integer 5 equals n + 1, continue)
#-> [-3 4 -5 -1] (integer 1 exists, value of index 0 negative)

#4. In the last loop, find the first index whose value is positive.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
	n=len(nums)
	for i in range(n):
	    if nums[i]>n or nums[i]<=0:
		nums[i]=n+1
	for i in range(n):
	    a=abs(nums[i])
	    if a==n+1:
		continue
	    nums[a-1]=-abs(nums[a-1])
	
	for i in range(n):
	    if nums[i]>0:
		return i+1
	return n+1	
