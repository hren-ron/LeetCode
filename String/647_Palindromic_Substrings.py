'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''

class Solution {
public:
    void help(string s,int i, int j, int &count){
        while(i>=0 && j<s.length() && s[i]==s[j]){
            i--;
            j++;
            count++;
        }
    }
    
    int countSubstrings(string s) {
        /*
        以字符串中的每一个字符都当作回文串中间的位置，然后向两边扩散，每当成功匹配两个左右两个字符，结果res自增1，然后再比较下一对。注意回文字符串有奇数和         偶数两种形式，如果是奇数长度，那么i位置就是中间那个字符的位置，所以我们左右两遍都从i开始遍历；如果是偶数长度的，那么i是最中间两个字符的左边那个，          右边那个就是i+1
        
        
        int n=s.length(),count=0;
        
        for(int i=0;i<n;i++){
            
            help(s,i,i,count);
            help(s,i,i+1,count);
        }
        
        return count;
        */
       
        /*
        
        使用动态规划算法来表示；
        dp[i][j]表示（i,j）是否是回文串
        如果s[i]==s[j],如果i=j,或者|i-j|=1,或者j-i=2,dp[i][j]=true;否则，dp[i][j]=dp[i-1][j+1]
        
        */
        
        int n=s.length(),count=0;
        
        vector<vector<bool>> dp(n,vector<bool>(n,false));
        
        for(int i=n-1;i>=0;i--){
            //dp[i][i]=true;
            
            for(int j=i;j<n;j++){
                
                //dp[i][j]=s[i]==s[j]&&(j-i<=2 || dp[i+1][j-1]);
                
                if(s[i]==s[j]){
                    
                    if(j-i<=2){
                        dp[i][j]=true;
                        //count++;
                    }
                    else
                        dp[i][j]=dp[i+1][j-1];
                }
                
                if(dp[i][j])
                    count++;
                
            }
        }
        return count;
        
        
        
    }
};
