'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''


class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if(k<1)
            return 0;
        int n=prices.size();
        if(n<=1)
            return 0;
        
        if(k>=n){
            int maxprofit=0;
            for(int i=1;i<n;i++){
                if(prices[i]>prices[i-1])
                    maxprofit+=prices[i]-prices[i-1];
            }
            return maxprofit;
                
        }
        
        vector<vector<int>> local(n,vector<int>(k+1,0));
        vector<vector<int>> global(n,vector<int>(k+1,0));
        
        for(int i=1;i<n;i++){
            int diff=prices[i]-prices[i-1];
            for(int j=1;j<=k;j++){
                local[i][j]=max(global[i-1][j-1],local[i-1][j]+diff);
                global[i][j]=max(global[i-1][j],local[i][j]);
            }
        }
        return global[n-1][k];
        
        /*
        vector<vector<int>> dp(n,vector<int>(n,0));
        vector<vector<bool>> flag(n,vector<bool>(n,true));
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                dp[i][j]=prices[j]-prices[i];
            }
        }
        int ans=0,pi=-1,pj=-1;
        while(k--){
            int price=INT_MIN;
            for(int i=pj+1;i<n-1;i++){
                for(int j=i+1;j<n;j++){
                    if(dp[i][j]>0&& flag[i][j] && dp[i][j]>price){
                        price=dp[i][j];
                        
                        pi=i;
                        pj=j;
                        cout<<'o'<<endl;
                    }
                        
                }
            }
            ans+=price;
            flag[pi][pj]=false;
        }
        return ans;
        */
        
    }
};