
'''
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        //int m=flights.size();
        
        /*
        最短路径问题:限制中转次数k，相当于飞k+1次
        dp[i][j]表示飞 i次时，到达j所需要的最小花费
        
        */
        int m=flights.size();
        vector<vector<int>> dp(K+2,vector<int>(n,1e9));
        dp[0][src]=0;
        
        for(int k=1;k<=K+1;k++){
            dp[k][src]=0;
            //cout<<k<<endl;
            for(int i=0;i<m;i++){
                //cout<<k-1<<dp[k-1][flights[i][0]]<<endl;
                dp[k][flights[i][1]]=min(dp[k][flights[i][1]],dp[k-1][flights[i][0]]+flights[i][2]);
            }
            
        }
        
        return dp[K+1][dst]>=1e9?-1:dp[K+1][dst];        
        
        
    }
};
