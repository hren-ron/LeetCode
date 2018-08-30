'''

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''


class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        
        int n=triangle.size();
        if(n==0)
            return 0;
        if(n==1)
            return triangle[0][0];
        
        /*
        vector<vector<int>> dp(n,vector<int>(n+1,0));
        
        dp[0][0]=triangle[0][0];
        int temp;
        for(int i=1;i<n;i++){
            
            temp=INT_MAX;
            for(int j=0;j<triangle[i].size();j++){
                if(j-1>=0 && j<i){
                    if(dp[i-1][j-1]<dp[i-1][j])
                        dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                    else
                        dp[i][j]=dp[i-1][j]+triangle[i][j];
                }
                
                    
                    
                else if(j-i<0)
                    dp[i][j]=dp[i-1][j]+triangle[i][j];
                else if(j>=i)
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                
                cout<<dp[i][j]<<endl;
                if(dp[i][j]<temp)
                    temp=dp[i][j];
                }
                
        }
        return temp;
        */
        
        /*
        对于一个data[i][j]，和它相邻的数字就是data[i+1][j]和data[i+1][j+1]。这样一来问题就简单了。假如我们用dp[i][j]来表示从第i行第j列处的数字开             始往下到最后一层的最小路径和，那么有:dp[i][j]=data[i][j]+min(dp[i+1][j],dp[i+1][j+1])
        
        在计算dp[i][j],需要用到dp[i+1][j+1],因此需要从后往前计算
        */
        
        int m=triangle[n-1].size();
        
        vector<int> dp(m,0);
        
        
        for(int i=0;i<m;i++)
            dp[i]=triangle[n-1][i];
        
        for(int i=n-2;i>=0;i--){
            
            for(int j=0;j<triangle[i].size();j++)
                dp[j]=min(dp[j+1],dp[j])+triangle[i][j];
        }
        
        return dp[0];
        
        
        
    }
};
