'''


Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''


class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        
        
        /*
        动态规划，求最长公共子串的方法
        */
        int n=A.size(),m=B.size();
        if(n==0 || m==0) return 0;
        
        vector<vector<int>> dp(n,vector<int>(m,0));
        
        int res=0;
        
        for(int i=0;i<n;i++)
            if(A[i]==B[0])
                dp[i][0]=1;
        for(int j=0;j<m;j++)
            if(A[0]==B[j])
                dp[0][j]=1;
        
        for(int i=1;i<n;i++)
            for(int j=1;j<m;j++)
                if(A[i]==B[j]){
                    dp[i][j]=dp[i-1][j-1]+1;
                    res=max(res,dp[i][j]);
                }
        return res;
    }
};