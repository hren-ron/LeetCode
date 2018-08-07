'''

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''


class Solution {
public:
    int numDistinct(string s, string t) {
        
        int m=s.length(),n=t.length();
        //cout<<n<<endl;
        if(n>m)
            return 0;
        
        /*
        
        无论T的字符与S的字符是否匹配，dp[i][j] = dp[i][j - 1].就是说，假设S已经匹配了j - 1个字符，得到匹配个数为dp[i][j - 1].现在无论S[j]是不是和T[i]   匹配，匹配的个数至少是dp[i][j - 1]。除此之外，当S[j]和T[i]相等时，我们可以让S[j]和T[i]匹配，然后让S[j - 1]和T[i - 1]去匹配
        
        假设t[i]表示t中第i个位置的前缀，s[j]表示s中第j个位置之前的前缀
        f[i][j]表示t[i]是s[j]的子集数量
        
        那么有状态转移矩阵：
        如果t[i-1]==s[j-1],f[i][j]=f[i-1][j-1]+f[i][j-1]
        否则f[i][j]=f[i][j-1]
        
        */
        
        vector<vector<int>> dp(n+1,vector<int>(m+1,0));
        //空集是任何集合的子集
        for(int i=0;i<m;i++)
            dp[0][i]=1;
        
        for(int i=1;i<n;i++)
            dp[i][0]=0;
        
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(s[j-1]==t[i-1])
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1];
                else
                    dp[i][j]=dp[i][j-1];
                //cout<<dp[i][j]<<endl;
            }
        }
        
        return dp[n][m];
        
    }
};