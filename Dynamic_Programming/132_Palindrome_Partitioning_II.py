'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''



class Solution {
public:
    int minCut(string s) {
        
       /*
       使用 dp[i]表示从i到最后的最小割的数量；
       如果[i,j]之间是回文串，那么dp[i]=min(dp[i],dp[j+1]+1)
       所以需要判断是否是回文串,可以把两个过程放在一起
       判断回文串也用动态规划，res[i][j]表示 s[i,j]是回文
       那么s[i]==s[j],s[i+1][j-1]=1,那么，s[i][j]=1
       
       */ 
        
        int n=s.length();
        vector<int> dp(n+1,0);
        vector<vector<bool>> res(n,vector<bool>(n,false));
        //dp[n]=0;
        
        for(int i=0;i<=n;i++)
            dp[i]=n-i-1;
        
        for(int i=n-1;i>=0;i--){
            
            for(int j=i;j<n;j++){
                //cout<<s[i]<<endl;
                
                if(s[i]==s[j] && (j-i<2 || res[i+1][j-1])){
                    res[i][j]=true;
                    dp[i]=min(dp[i],dp[j+1]+1);
                }
                
                
            }
        }
    
        return dp[0];
        
    }
};
