'''

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''


class Solution {
public:
    
    int findTargetSumWays(vector<int>& nums, int S) {
        
        /*
        使用动态规划，因为最大值只能是1000，但是有正负值，因此可以申请一个长度为2001的列表，下标代表可能达到的值
        dp[i][k+nums[i]+1000]=dp[i-1][k+1000],当在前一个元素达到k时，目前达到k+nums[i]
        dp[i][k-nums[i]+1000]=dp[i-1][k+1000],当在前一个元素达到k时，目前达到k-nums[i]
        */
        
        if(S>1000)
            return 0;
        
        int n=nums.size();
        
        vector<vector<int>> dp(n,vector<int>(2001,0));
        dp[0][nums[0]+1000]=1;
        
        //避免开头的元素为0，那样的话会有两种方式
        dp[0][-nums[0]+1000]+=1;
        
        for(int i=1;i<n;i++){
            
            for(int k=-1000;k<=1000;k++){
                
                if(dp[i-1][k+1000]>0){
                    dp[i][k+nums[i]+1000]+=dp[i-1][k+1000];
                    dp[i][k-nums[i]+1000]+=dp[i-1][k+1000];
                }
                
            }
            
        }
        
        return dp[n-1][S+1000];
        
        
    }
    
    /*
    暴力搜索
    int count=0;
    int findTargetSumWays(vector<int>& nums, int S) {
        
        find(nums,0,0,S);
        
        return count;
        
    }
    
    void find(vector<int> &nums,int i,int sum,int S){
        
        if(i==nums.size()){
            if(sum==S)
                count++;
            
        }else{
            find(nums,i+1,sum+nums[i],S);
            find(nums,i+1,sum-nums[i],S);
        
        }
        
    }
    */
};