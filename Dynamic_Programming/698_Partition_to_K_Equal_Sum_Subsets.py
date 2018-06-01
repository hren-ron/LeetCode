'''

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''


class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        
        int n=nums.size();
        int sum=0,target;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        if(sum%k!=0)
            return false;
        target=sum/k;
        //cout<<"o";
        vector<bool> isUsed(n,false);
        return can(nums,isUsed,k,target,0,0);
        
    }
    
    bool can(vector<int> &nums,vector<bool> &isUsed,int k,int target,int index,int curSum){
        if(k==0)
            return true;
        if(curSum==target)
            return can(nums,isUsed,k-1,target,0,0);
        for(int i=index;i<nums.size();i++){
            if(isUsed[i]) 
                continue;
            isUsed[i]=true;
            
            if (can(nums, isUsed, k, target, i + 1, curSum + nums[i])) {
                return true;
            }
            /*
            if(can(nums,isUsed,k,target,i+1;curSum+nums[i])){
                return true;
            }
            */
                
            isUsed[i]=false;
        }
        return false;
    }
};
