'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

'''

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        row=len(matrix)
        col=len(matrix[0])
        
        poss=[(row-1,0)]
        for i in range(row+col-1):
            temp=[]
            for pos in poss:
                if(pos[0]-1>=0 and pos[1]+1<col):
                    temp.append((pos[0]-1,pos[1]))
                    temp.append((pos[0],pos[1]+1))
            poss=list(set(temp))
            if(poss):
                for i in range(1,len(poss)):
                    if(matrix[poss[i][0]][poss[i][1]]!=matrix[poss[i-1][0]][poss[i-1][1]]):
                        return(False)
        return(True)
