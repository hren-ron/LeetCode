'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


主要考虑矩阵对角线上的值，右底的值等于上面的加上前面的
d=[[1,1],[1,2]],d[i][j]=d[i-1][j]+d[i][j-1]

'''


class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int m=obstacleGrid.size(),n=obstacleGrid[0].size();
        vector<vector<int>> ans(m,vector<int>(n,0));
        
        for(int i=0;i<m;i++){
            if(!obstacleGrid[i][0])
                ans[i][0]=1;
            else
                break;
        }
        
        for(int j=0;j<n;j++){
            if(!obstacleGrid[0][j])
                ans[0][j]=1;
            else
                break;
        }
        //cout<<ans[0][1];
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                if(obstacleGrid[i][j])
                    ans[i][j]=0;
                else{
                    ans[i][j]=ans[i-1][j]+ans[i][j-1];
                }
            }
        }
        return ans[m-1][n-1];
        
        
        
    }
};