'''

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


'''

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        if(len(nums)==0 or len(nums)==1):
            return(False)
        new_nums=sorted(nums)
        
        for i in range(1,len(nums)):
            if(new_nums[i] == new_nums[i-1]):
                return(True)
        return(False)
        '''
        
        new_list=list(set(nums))
        if(len(new_list)==len(nums)):
            return(False)
        else:
            return(True)