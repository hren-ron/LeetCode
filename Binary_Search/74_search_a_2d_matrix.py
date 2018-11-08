'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

'''
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        
        
        /*
        
        方法1：

        将二维数组按行展开的话，就是一个排序的一维数组，因此通过一维数组的二分查找很容易得到答案。
        
        if (matrix.empty() || matrix[0].empty()) return false;
        if (target < matrix[0][0] || target > matrix.back().back()) return false;
        int m = matrix.size(), n = matrix[0].size();
        int left = 0, right = m * n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (matrix[mid / n][mid % n] == target) return true;
            else if (matrix[mid / n][mid % n] < target) left = mid + 1;
            else right = mid - 1;
        }
        return false;
        
        
        方法2：

        鉴于数组的规律性，选取数组查找范围的右上角数字，如果与查找的数字相等， 则返回true，如果比查找的数字大，则从后面的                   行开始找，如果比查找数字小，则从前面的列中开始找。

        方法3：

        先通过二分查找元素所在的行，再在所在行通过二分查找元素。
        */
        
        if (matrix.empty() || matrix[0].empty())
             return false;
        if (target < matrix[0][0] || target > matrix.back().back())
            return false;
        
        int row=0,col=matrix[0].size()-1;
        
        while(row<matrix.size() && col>=0){
            if(matrix[row][col]==target)
                return true;
            if(matrix[row][col]>target)
                col--;
            else
                row++;
        }
        return false;
        
        
    }
};
