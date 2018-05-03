'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

'''

#可以不用排序，直接找到两个较小的元素以及较大的三个元素


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        if(length==3):
            return(nums[0]*nums[1]*nums[2])
        new_nums=sorted(nums)
        
        if(new_nums[0]>=0 or new_nums[-1]<=0):
            return(new_nums[-1]*new_nums[-2]*new_nums[-3])
        else:
            if(new_nums[0]*new_nums[1]>new_nums[-2]*new_nums[-3]):
                return(new_nums[0]*new_nums[1]*new_nums[-1])
            else:
                return(new_nums[-1]*new_nums[-2]*new_nums[-3])
            