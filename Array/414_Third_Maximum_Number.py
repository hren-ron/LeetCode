'''

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''



class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if(len(set(nums))<3):
            return(max(nums))
        min1=float('-inf')
        min2=float('-inf')
        min3=float('-inf')
        
        for n in set(nums):
            if(n>min3):
                min1=min2
                min2=min3
                min3=n
            elif(n>min2):
                min1=min2
                min2=n
            elif(n>min1):
                min1=n
        return(min1)
        