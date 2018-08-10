'''
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.

'''

class Solution {
public:
    /*
    int stone_game(vector<vector<int>>& piles,int dp[501][501][2],int i,int j,int flag){
        
        if(i>j)
            return 0;
        if(dp[i][j][flag])
            return dp[i][j][flag];
        
        if(flag){
            return(dp[i][j][flag]=max(piles[i] + stone_game(piles,dp,i+1,j,false),piles[j-1]+stone_game(piles,dp,i,j-1,false)));
            return dp[i][j][flag];
        }else{
            dp[i][j][flag]=min(stone_game(piles,dp,i+1,j,true),stone_game(piles,dp,i,j-1,true));
            return dp[i][j][flag];
        }
    }
    */
    
    bool stoneGame(vector<int>& piles) {
        
        //如果只有两个pile，Alex肯定会赢；类似的，如果有四个pile，那么分成两份，每次从两份中选择最大的pile，也是Alex赢
        //
        //return true;
        
        /*
        该问题的子问题是，相邻两堆的石头的胜负，然后求相邻3堆石头的胜负，最后原问题是相邻n堆石头的胜负
        使用dp[i][j]表示从 piles[i]-piles[j]中Alex可以多的石头数，所以状态转移方程式
        dp[i][j]=max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1]).
        因为两个人都采用最优的方法，当Alex选择piles[i]或者piles[j]时，然后该Lee先选，所以应该减去Lee赚的
        
        */
        
        int n=piles.size();
        vector<vector<int>> dp(n,vector<int>(n,0));
        
        for(int i=0;i<n;i++)
            dp[i][i]=piles[i];
        
        for(int len=1;len<n;len++){
            for(int i=0;i<n-len;i++){
                dp[i][i+len]=max(piles[i]-dp[i+1][i+len],piles[i+len]-dp[i][i+len-1]);
            }
        }
        
        return dp[0][n-1]>0?true:false;
        
        
        /*
        采用递归的方法
        
        dp[i][j][0],在piles[i]-piles[j]之间 Lee的石子数
        dp[i][j][1],Alex取得石子数
        */
        /*
        int sum=0;
        for(int i=0;i<piles.size();i++)
            sum+=piles[i];
        
        int dp[501][501][2] = {0};
        
        int count=stone_game(piles,dp,0,piles.size(),true);
        
        return count*2>sum;
        */
    }
};
