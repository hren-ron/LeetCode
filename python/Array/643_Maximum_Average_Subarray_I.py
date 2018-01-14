'''
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

'''


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        '''
        counts=[]
        
        for i in range(len(nums)-k+1):
            
            temp=0
            for j in range(i,i+k):
                temp+=nums[j]
                #print(nums[j])
            counts.append(temp/k)
            #break
        return(max(counts))
        '''
        count=0
        for i in range(k):
            count+=nums[i]
        res=count
        for i in range(k,len(nums)):
            count=count+nums[i]-nums[i-k]
            res=max(res,count)
        return(res/k)
