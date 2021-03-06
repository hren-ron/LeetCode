'''

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
        int m=grid.size(),n=grid[0].size();
        int a[m][n];
        a[0][0]=grid[0][0];
        for(int i=1;i<m;i++)
            a[i][0]=a[i-1][0]+grid[i][0];
        for(int i=1;i<n;i++)
            a[0][i]=a[0][i-1]+grid[0][i];
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                a[i][j]=min(a[i-1][j],a[i][j-1])+grid[i][j];
            }
        }
        return a[m-1][n-1];
        
        
        
    }
};
