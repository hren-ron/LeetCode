'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution {
public:
    string longestPalindrome(string s) {
        /*
        int n=s.length();
        int i=0,j=n-1;
        string dp;
        stack<char> stk;
        while(j>=i){
            if(j==i){
                dp=dp+s[i];
                i++;
                j--;
                continue;
            }else{
                if(s[i]==s[j]){
                    dp=dp+s[i];
                    stk.push(s[j]);
                    i++;
                    j--;
                }else{
                    dp="";
                    while(!stk.empty())
                        stk.pop();
                    j--;
                }
                    
            }
        }
        if(!stk.empty()){
            char c;
            c=stk.top();
            stk.pop();
            dp=dp+c;
        }
        return dp;
       
        
        int n=s.length();
        
        int optimalStart = 0; 
        int optimalEnd = 0;
        vector<vector<int>> dp(n,vector<int>(n,0));
        
        for(int i=0;i<n;i++){
            dp[i][i]=1;
        }
        for(int i=1;i<n;i++){
            if(s[i]==s[i-1]){
                 dp[i][i+1]=2;
            }
                
        }
        for(int i=0;i<n-2;i++){
            for(int j=i+2;j<n;j++){
                if(s[i]==s[j] && dp[i+1][j-1]>0)
                    dp[i][j]=dp[i+1][j-1]+2;
            }
        }
      
        int temp=0,start=0,end=0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(temp<dp[i][j]){
                    temp=dp[i][j];
                    start=i;
                    end=j;
                    
                }
            }
        }
       
        return s.substr(start,temp);
         */
        
        
        int len = s.length();
        int optimalStart = 0; 
        int optimalEnd = 0;

        vector<vector<bool>> solution;
        solution.resize(len);
        for_each(solution.begin(), solution.end(), [len](auto& v) {
            v.resize(len, false);
        });

      
        for (int i = 0; i < len; i++)
            solution[i][i] = true;

       
        for (int i = 1; i < len; i++)
        {
            if (s[i] == s[i - 1])
            {
                solution[i - 1][i] = true;
                if (2 > optimalEnd - optimalStart)
                {
                    optimalStart = i - 1;
                    optimalEnd = i;
                }
            }
        }

        
        for (int step = 3; step - 1 < len; step += 1)
        {                
            for (int i = step; i - 1 < len; i++)
            {                  
                int start = i - step, end = i - 1;
                if (solution[start + 1][end - 1] && s[start] == s[end])
                {
                    solution[start][end] = true;
                    if (end - start > optimalEnd - optimalStart)
                    {
                        optimalStart = start;
                        optimalEnd = end;
                    }
                }
            }
        }

        return s.substr(optimalStart, optimalEnd - optimalStart + 1);
        
    }
};
