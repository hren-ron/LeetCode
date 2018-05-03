'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        if(len(nums)==1):
            return(1)
        nums_set=list(set(nums))
        
        num_count=[]
        for n in nums_set:
            num_count.append(nums.count(n))
        
        degrees=[]
        degree=max(num_count)
        for i in range(len(num_count)):
            if(num_count[i]==degree):
                degrees.append(nums_set[i])
        counts=[]
        for d in degrees:
            
            indexs=[]
            for i in range(len(nums)):
                if(nums[i]==d):
                    indexs.append(i)
            counts.append(max(indexs)-min(indexs)+1)
        return(min(counts))
        """
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
        