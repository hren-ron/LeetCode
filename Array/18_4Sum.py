
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        
        
        
        /*
        先固定两个数，然后计算另外两个数的和;
        要可以进行的有三个地方，首先在两个for循环下可以各放一个，因为一旦当前的数字跟上面处理过的数字相同了，那么找下来肯定还是重复的。之后就是当sum等于target的时候了，我们在将四个数字加入结果res之后，left和right都需要去重复处理，分别像各自的方面遍历即可
        
        */
        int n=nums.size(),k=0;
        vector<vector<int>> res;
        if(n<4) return res;
        
        sort(nums.begin(),nums.end());
        
        for(int i=0;i<n-3;i++){
            if(i>0 && nums[i]==nums[i-1])
                continue;
            for(int j=i+1;j<n-2;j++){
                if(j>i+1 && nums[j]==nums[j-1])
                    continue;
                int left=j+1,right=n-1;
                
                while(left<right){
                    
                    if(nums[left]+nums[right]+nums[i]+nums[j]==target){
                        vector<int> temp;
                        temp.push_back(nums[left]);
                        temp.push_back(nums[right]);
                        temp.push_back(nums[i]);
                        temp.push_back(nums[j]);
                        res.push_back(temp);
                        
                        while(left<right && nums[left]==nums[left+1]) left++;
                        while(left<right && nums[right]==nums[right-1]) right--;
                        
                        left++;
                        right--;
                    }else if(nums[left]+nums[right]+nums[i]+nums[j]<target)
                             left++;
                        else
                             right--;
                }
            }
        }
        return res;
    }
};
