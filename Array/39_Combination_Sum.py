
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

'''


class Solution {
public:
    vector<int> ans;
    vector<vector<int>> res;
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        
        /*
        使用回溯法
        */
        
        dfs(0,0,target,candidates);
        return res;
        
    }
    
    void dfs(int start,int sum,int target,vector<int> &candidates){
        if(sum==target){
            res.push_back(ans);
            return;
        }else if(sum>target)
            return;
        else{
            for(int i=start;i<candidates.size();i++){
                ans.push_back(candidates[i]);
                dfs(i,sum+candidates[i],target,candidates);
                ans.pop_back();
            }
        }
        
    }
};






