
'''

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        /*
        类似于矩阵链乘问题。
        dp[i][j]表示在（i，j）之间最后爆炸的气球k，而不是用最先爆炸的气球是k，因为这样的话，左右两个子序列并不是独立的。
        因此状态转移方程式:dp[i][j]=max(dp[i][j],nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j])
        自底向上开始计算
        */
        int m=nums.size();
        nums.insert(nums.begin(),1);
        nums.push_back(1);
        
        int n=nums.size();
        vector<vector<int>> dp(n,vector<int>(n,0));
        
        for(int k=1;k<=m;k++){
            for(int i=1;i<=m-k+1;i++){
                int j=i+k-1;
                cout<<i<<endl;
                for(int p=i;p<=j;p++)
                    dp[i][j]=max(dp[i][j],nums[i-1]*nums[p]*nums[j+1]+dp[i][p-1]+dp[p+1][j]);
                cout<<dp[i][j]<<endl;
            }
        }
        return dp[1][m];
    }
};