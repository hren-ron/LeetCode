'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

class Solution {
public:
    bool isScramble(string s1, string s2) {
        
        /*
        关键思想在于：如果s1和s2是相互scramble，那么如果把s1分成s11,s12，将s2分成s21,s22；
        存在s11和s21互相scramble并且s12和s22互相scramble,或者s11和s22是scramble并且s12和s21是scramble;
        
        因此，如果使用动态规划，dp[i][j][n]表示s1从i开始，s2从j开始，长度为n的字符串是不是相互scramble；
        根据上面的思想，长度为n的字符串，如果分成子串的话，会有n-1种方法
        */
        
        if(s1==s2)
            return true;
        int n=s1.length(),m=s2.length();
        
        if(n!=m)
            return false;
        
        vector<vector<vector<bool>>> dp(n,vector<vector<bool>>(n,vector<bool>(n+1,false)));
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                dp[i][j][1]=s1[i]==s2[j];
            }
        }
        
        for(int len=2;len<=n;len++){
            for(int i=0;i<=n-len;i++){
                for(int j=0;j<=n-len;j++){
                    for(int k=1;k<len;k++){
                        if(dp[i][j][k] && dp[i+k][j+k][len-k] || dp[i][j+len-k][k] && dp[i+k][j][len-k])
                            dp[i][j][len]=true;
                    }
                    
                }
            }
            
        }
        
        
        return dp[0][0][n];
        
        
        
    }
};

