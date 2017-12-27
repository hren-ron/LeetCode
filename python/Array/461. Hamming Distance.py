'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x_s=bin(x)[2:]
        y_s=bin(y)[2:]
        print(x_s)
        print(y_s)
        x_s=list(reversed(x_s))
        y_s=list(reversed(y_s))
        count=0
        print(x_s)
        print(y_s)
        if(len(x_s)==len(y_s)):
            
            for i in range(len(x_s)):
            
                if(x_s[i]!=y_s[i]):
                    count=count+1
        if(len(x_s)>len(y_s)):
            for i in range(len(x_s)):
                if(i>=len(y_s)):
                    if(x_s[i]!='0'):
                        count=count+1
                else:
                    if(x_s[i]!=y_s[i]):
                        count=count+1
        if(len(x_s)<len(y_s)):
            for i in range(len(y_s)):
                if(i>=len(x_s)):
                    if(y_s[i]!='0'):
                        count=count+1
                else:
                    if(x_s[i]!=y_s[i]):
                        count=count+1
        return(count)
            
                

