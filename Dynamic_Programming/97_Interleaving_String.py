'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

'''
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        
        /*
        使用动态规划的方法：
        使用dp[i][j]表示s1的前i个字符与s2的前j个字符能够组成s3的（i+j）个字符
        
        因为s3中每一个位置只有一个字符，因此，如果要形成s3中前(i+j)个前缀:
        只有两种情况：从s1的前（i-1）个字符和s2的前（j）个字符，比较s1[i-1]和s3[i-1+j];
        反之，另外一种
        
        可以看出，其实只有两种方式来递推，一种是选取s1的字符作为s3新加进来的字符，另一种是选s2的字符作为新进字符。
		而要看看能不能选取，就是判断s1(s2)的第i(j)个字符是否与s3的i+j个字符相等。
		如果可以选取并且对应的res[i-1][j](res[i][j-1])也为真，就说明s3的i+j个字符可以被表示。
		这两种情况只要有一种成立，就说明res[i][j]为真，是一个或的关系。
        */
        
        int m=s1.length(),n=s2.length(),p=s3.length();
        
        if(m+n!=p)
            return false;
        if(m==0 && n==0 && p==0)
            return true;
        vector<vector<bool>> dp(m+1,vector<bool>(n+1,false));
        dp[0][0]=true;
        for(int i=1;i<=m;i++){
            dp[i][0]=(s1[i-1]==s3[i-1]) && dp[i-1][0];
        }
        for(int i=1;i<=n;i++)
            dp[0][i]=(s2[i-1]==s3[i-1]) && dp[0][i-1];
        
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                dp[i][j]=(s1[i-1]==s3[i+j-1]) && dp[i-1][j] ||(s2[j-1]==s3[i+j-1]) && dp[i][j-1];
            }
        }
        return dp[m][n];
        
    }
};
