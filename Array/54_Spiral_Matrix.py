
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        /*
        按照四个方向进行循环遍历
        */
        
        vector<int> res;
        if(matrix.empty() || matrix[0].empty()) return res;
        
        int m=matrix.size(),n=matrix[0].size();
        
        
        int up=0,bottom=m-1,left=0,right=n-1;
        while(true){
            for(int i=left;i<=right;i++) res.push_back(matrix[up][i]);
            if(++up>bottom) break;
            
            for(int i=up;i<=bottom;i++) res.push_back(matrix[i][right]);
            
            if(--right<left) break;
            
            for(int i=right;i>=left;--i) res.push_back(matrix[bottom][i]);
            if(--bottom<up) break;
            
            for(int i=bottom;i>=up;--i) res.push_back(matrix[i][left]);
            if(++left>right) break;
            
        }
        return res;
        
        
    }
};