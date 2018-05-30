'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

'''



class Solution {
public:
    
   
    int getMoneyAmount(int n) {
        
        if(n==1)
            return 0;
        //a[i,j]=k+max(a[i,k-1],a[k+1,j])
        
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        
       
        
        for(int i=2;i<n+1;i++){
            for(int j=i-1;j>0;j--){
                if(j==i-1)
                    dp[j][i]=j;
                else{
                    int res=INT_MAX;
                    for(int k=j+1;k<i;k++){
                        int temp=k+max(dp[j][k-1],dp[k+1][i]);
                        if(temp<res)
                            res=temp;
                    }
                    dp[j][i]=res;
                }
                
            }
        }
        return dp[1][n];
       
        
    
        
    }
    /*
     int get_num(int **a,int start,int end){
        if(start<=end)
            return 0;
        if(a[start][end]!=0)
            return a[start][end];
        
        int res=INT_MAX;
        for(int i=start;i<=end;i++){
            int temp=i+max(get_num(a,start,i-1),get_num(a,i+1,end));
            if(temp<res)
                res=temp;
        }
        a[start][end]=res;
        return res;
        
        
    }
    */
};


