
'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        /*
        我们可以一位一位的网上叠加，比如对于题目中给的例子[1,2,3]来说，最开始是空集，那么我们现在         要处理1，就在空集上加1，为[1]，现在我们有两个自己[]和[1]，下面我们来处理2，我们在之前的子集基础上，每个都加个2，可以分别得到[2]，[1, 2]，那么现在所有的子集合为[], [1], [2], [1, 2]，同理处理3的情况可得[3], [1, 3], [2, 3], [1, 2, 3], 再加上之前的子集就是所有的子集合了
        
        
        vector<vector<int>> res(1);
        int n=nums.size();
        sort(nums.begin(),nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            int size = res.size();
            for (int j = 0; j < size; ++j) {
                res.push_back(res[j]);
                res.back().push_back(nums[i]);
            }
        }
        return res;
        
        */
        
        /*
        使用深度优先搜索的方法，每个元素要不加入，要不然就加入
        对于每位使用二进制之表示
        */
        
        vector<vector<int>> res;
        
        vector<int> result;
        sort(nums.begin(),nums.end());
        
        dfs(nums,0,result,res);
        return res;
        
        
    }
    void dfs(vector<int> &nums,int pos,vector<int> &result,vector<vector<int>> &res){
        res.push_back(result);
        
        for(int i=pos;i<nums.size();i++){
            result.push_back(nums[i]);
            dfs(nums,i+1,result,res);
            result.pop_back();
        }
    }
};