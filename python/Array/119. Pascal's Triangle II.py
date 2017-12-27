
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?



'''

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        nums=[]
        
        for i in range(rowIndex+1):
            if(i==0):
                nums.append([1])
                continue
            if(i==1):
                nums.append([1,1])
                continue
            temp=[1]*(i+1)
            for j in range(1,i):
                
                temp[j]=nums[i-1][j-1]+nums[i-1][j]
            nums.append(temp)
        return(nums[rowIndex])
        """
        
        for i in range(rowIndex+1):
            if(i==0):
                temp=[1]
                continue
            if(i==1):
                temp=[1,1]
                continue
            new_temp=[1]*(i+1)
            for j in range(1,i):
                new_temp[j]=temp[j-1]+temp[j]
            temp=new_temp
        return(temp)