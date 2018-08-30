'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        
        int n=s.length();
        
        if(n<=1)
            return n;
        
        /*
        求原问题的子问题，该字符串的子串的最长回文的长度；
        假设dp[i][j]表示从i-j之间的子串的最大回文字符串的长度
        如果s[i]==s[j],dp[i][j]=dp[i+1][j-1]+2
        如果s[i]!=s[j],dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        
        其实该问题可以转换为 求s和s的逆排序的最长公共子序列问题；
        
        */
        
        vector<vector<int>> dp(n,vector<int>(n,0));
        
        for(int i=n-1;i>=0;i--){
            dp[i][i]=1;
            
            for(int j=i+1;j<n;j++){
                if(s[i]==s[j])
                    dp[i][j]=dp[i+1][j-1]+2;
                else
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
            }
            
        }
        return dp[0][n-1];
        
        
        
        /*
        vector<int> dp(n,1);
    
        int temp=0,max=INT_MIN;
        for(int i=1;i<n;i++){
            if(s[i]==s[i-1]){
                dp[i]=dp[i-1]+1;
                temp=i;
            }
                
            else{
                for(int j=temp;j<i;j++){
                    if(s[j]==s[i]){
                        dp[i]=dp[j]+1;
                    }
                }
            }
            
            if(dp[i]>max)
                max=dp[i];
        }
        
        return max;
        */
        
    }
};
