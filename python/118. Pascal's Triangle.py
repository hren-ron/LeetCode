'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

明显是一个动态规划问题，
当然有一些技巧性方法，比如：
 	1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        nums=[]
        for i in range(numRows):
            if(i==0):
                nums.append([1])
                continue
            if(i==1):
                nums.append([1,1])
                continue
            temp=[]
            temp.append(1)
            for j in range(len(nums[i-1])-1):
                temp.append(nums[i-1][j]+nums[i-1][j+1])
            temp.append(1)
            nums.append(temp)
        return(nums)
                