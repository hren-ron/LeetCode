'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        num_sort=sorted(nums)
        
        if(n==1):
            return(nums[0])
        count=1
        for i in range(1,n):
            
            if(num_sort[i]==num_sort[i-1]):
                count+=1
                if(count>int(n/2)):
                    return(num_sort[i-1])
                    
            else:
                count=1
                
          
