'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''


class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        
        int n=s.length(),m=wordDict.size();
        vector<string> res;
        /*
        采用递归的方法：
        在wordDict中遍历，如果某个单词是s的开头单词，那么就从s中下个位置继续遍历；
        因为要用到重复的，所以建立字典映射；
        */
        unordered_map<string,vector<string>> dp;
        
        
        
        
        return words(s,wordDict,dp);
        
    }
    
    
    vector<string> words(string s,vector<string> &wordDict,unordered_map<string,vector<string>> &dp){
        
        if(dp.count(s))
            return dp[s];
        if(s.empty())
            return {""};
        
        vector<string> res;
        for(string word:wordDict){
            
            if(s.substr(0,word.length())!=word)
                continue;
            vector<string> rem=words(s.substr(word.length()),wordDict,dp);
            
            for(string str:rem){
                res.push_back(word+(str.empty()?"":" ")+str);
            }
            
        }
        return dp[s]=res;
        
    }
};