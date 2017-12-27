'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.

'''

'''
也可以记录下下标，因为如果[i,j]是最长递增的子列表，那么nums[i-1]>=nums[i],nums[j+1]<=nums[j]
'''


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return(0)
        counts=[]
        count=1
        for i in range(len(nums)-1):
            if(nums[i+1]>nums[i]):
                count=count+1
                counts.append(count)
                #continue
            else:
                counts.append(count)
                count=1
            
        print(counts)
        if(counts):
            return(max(counts))
        else:
            return(count)
