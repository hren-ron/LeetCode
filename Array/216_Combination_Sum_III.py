'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        
        
        /*
        递归的方法：对于每个数字有选择或不选择两个选项。选择k个数计算它们的和
        深度优先搜索
        */
        
        vector<vector<int>> res;
        
        vector<int> ans;
        if(n==0 || k==0) return res;
        
        dfs(k,n,1,ans,res);
        return res;
        
        
    }
    void dfs(int k,int n,int start,vector<int> &ans,vector<vector<int>> &res){
        if(n<0) return;
        if(n==0 && ans.size()==k) res.push_back(ans);
        
        for(int i=start;i<=9;i++){
            ans.push_back(i);
            dfs(k,n-i,i+1,ans,res);
            ans.pop_back();
        }
    }
    
};

