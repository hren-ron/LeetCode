'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        /*
        从矩阵的右上角开始探索。若当前 元素比 target小，当前行加一，若大，当前列减一。若 当前元素等于target ，返回True。若 当前 行 或 列 越界，则返回 False。
        同样可以从左下搜索，若目标大于该位置的元素，则col++;目标小于该位置的元素，则row--;
        */
        if(matrix.empty() || matrix[0].empty())
            return false;
        int m=matrix.size(),n=matrix[0].size();
        
        int row=0,col=n-1;
        while(row<m && col>=0){
            
            if(matrix[row][col]==target)
                return true;
            else if(matrix[row][col]>target)
                col--;
            else
                row++;
        }
        return false;
    }
};