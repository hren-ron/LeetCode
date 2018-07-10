'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        
        /*
        假设现在构成 i（i<=amount），dp[i]表示构成 i时所需要的最小的钱的数量，那么在选择时，每次可以从 coins中选择一个元素，
        但是并不知道选择哪个，因此需要遍历 coins。
        假设现在选择 coins[j],那么 dp[i]=dp[i-coins[j]]+1;
        所以在每次遍历时，求最小，dp[i]=min(dp[i],dp[i-coins[j]]+1)
        */
        int n=coins.size();
        vector<int> dp(amount+1,amount+1);
        dp[0]=0;
        for(int i=1;i<=amount;i++){
            for(int j=0;j<n;j++){
                if(coins[j]<=i)
                    dp[i]=min(dp[i],dp[i-coins[j]]+1);
                
            }
        }
        /*
        for(int i=1;i<=amount;i++)
            cout<<dp[i]<<endl;
        */
        return dp[amount]>amount?-1:dp[amount];
        
       
    }
};