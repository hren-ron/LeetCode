'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''





class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        /*
        先固定一个数，然后找另外两个数字为第一个数字的负数；
        找的时候可以先排序，然后使用双指针的方法来判断两个数字之和；
        
        需要剪枝：1，如果当前数为正数，说明以后的数也是正数，则不可能是0；
        2.如果后一个数字重复，则去重，跳过这个数字
        */
        
        vector<vector<int>> res;
        int n=nums.size();
        if(n<3) return res;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++){
            if(nums[i]>0) break;
            if(i>0 && nums[i]==nums[i-1]) continue;
            
            int j=i+1,k=n-1;
            while(j<k){
                if(nums[j]+nums[k]==-nums[i]){
                    res.push_back({nums[i],nums[j],nums[k]});
                    while (j < k && nums[j] == nums[j + 1]) ++j;
                    while (j < k && nums[k] == nums[k - 1]) --k;
                    j++;
                    k--;
                    
                }else if(nums[j]+nums[k]>-nums[i])
                    k--;
                else
                    j++;
            }
        }
        return res;
    }
};