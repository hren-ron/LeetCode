'''

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
         
        if (not nums):
            return 0

        len = 0

        for i in range(1, len(nums)):
            if A[i] != A[len]:
                len += 1
                A[len] = A[i]

        return (len + 1)
        
        """
        if(not nums):
            return(0)
        indexs=[]
        for i in range(1,len(nums)):
            if(nums[i-1]==nums[i]):
                indexs.append(i)
        #print(indexs)
        temp=0
        for i in indexs:
            
            del nums[i-temp]
            temp=temp+1
            #nums.remove(nums[i])
        return(len(nums))
       