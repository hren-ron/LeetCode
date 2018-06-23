'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''


class Solution {
public:
    bool contains(string s,vector<string> & wordDict){
        int n=wordDict.size();
       
        for(int i=0;i<n;i++){
            
            if(s==wordDict[i])
                
                return true;
        }
       
        return false;
    }
   
    bool wordBreak(string s, vector<string>& dict) {
        
        
        if(dict.size()==0) return false;
        
        vector<bool> dp(s.size()+1,false);
        dp[0]=true;
        
        for(int i=1;i<=s.size();i++)
        {
            for(int j=i-1;j>=0;j--)
            {
                if(dp[j])
                {
                    string word = s.substr(j,i-j);
                    if(find(dict.begin(),dict.end(),word)!= dict.end())
                    {
                        dp[i]=true;
                        break; //next i
                    }
                }
            }
        }
        
        return dp[s.size()];
        /*
        int n=s.length();
        vector<bool> dp(n+1,false);
        dp[0]=true;
        //bool *dp=new bool[n];
        //cout<<n;
        for(int i=1;i<=n;i++){
            
            if(contains(s.substr(0,i+1),wordDict)){
                dp[i]=true;
                continue;
            }
           
            for(int j=0;j<i;j++){
                
                if(dp[j] && contains(s.substr(j+1,i+1),wordDict)){
                    dp[i]=true;
                   
                    break;
                }
            }\
        
           
        }
        /*
        for(int i=0;i<n;i++)
            cout<<dp[i]<<endl;;
        //cout<<dp[n-6];
        
        //cout<<dp.size();
       return dp[n-1]; 
    */
        
        
    }

    
    
};
