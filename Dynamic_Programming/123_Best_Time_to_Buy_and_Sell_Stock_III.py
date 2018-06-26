'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int n=prices.size();
        if(n<=1)
            return 0;
        
        
        int *former=new int[n];
        int minPrice=prices[0];
        former[0]=0;
        for(int i=1;i<n;i++){
            minPrice=min(minPrice,prices[i]);
            former[i]=max(former[i-1],prices[i]-minPrice);
        }
        
        int *later=new int[n];
        later[n-1]=0;
        int maxPrice=prices[n-1];
        for(int i=n-2;i>=0;i--){
            maxPrice=max(maxPrice,prices[i]);
            later[i]=max(maxPrice-prices[i],later[i+1]);
            cout<<maxPrice;
        }
        
        int profit=INT_MIN;
        for(int i=0;i<n;i++){
            profit=max(profit,former[i]+later[i]);
            
        }
        return profit;
        /*
        int profit_count=0,count=0;
        int *save=new int[n];
        int *sell=new int[n];
        int *profits=new int[n];
        save[0]=-prices[0],sell[0]=0;
        
        for(int i=1;i<n;i++){
            save[i]=max(save[i-1],sell[i-1]-prices[i]);
            if(save[i-1]+prices[i]>sell[i-1]){
                
                sell[i]=save[i-1]+prices[i];
                profits[count++]=sell[i]-profit_count;
                cout<<i<<sell[i-1]<<profit_count<<endl;
                profit_count=sell[i];
            }else{
                sell[i]=sell[i-1];
            }
        }
        
        int max1=0,max2=0;
        for(int i=0;i<count;i++){
            //cout<<profits[i]<<endl;
            if(profits[i]>0 && profits[i]>max1){
                max2=max1;
                max1=profits[i];
            }else if(profits[i]>0 && profits[i]>max2)
                max2=profits[i];
            
        }
        return (max1+max2);
        */
        
        
    }
};