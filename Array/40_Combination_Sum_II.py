'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        
        
        /*
        dfs的方法，但是要去除重复的元素
        */
        
        vector<vector<int>> res;
        vector<int> temp;
        //vector<bool> visit(candidates.size(),false);
        sort(candidates.begin(),candidates.end());
        dfs(0,target,candidates,temp,res);
        return res;
    }
    
    
    void dfs(int start,int target,vector<int> &candidates,vector<int> &tmp,vector<vector<int>> &res){
        
        if(target==0){
            res.push_back(tmp);
            return;
        }else if(target<0)
            return;
        else{
            for(int i=start;i<candidates.size();i++){
                if(i>start && candidates[i]==candidates[i-1])
                    continue;
                
                    
                tmp.push_back(candidates[i]);
                dfs(i+1,target-candidates[i],candidates,tmp,res);
                tmp.pop_back();
                    
                
            }
        }
        
        
    }
};