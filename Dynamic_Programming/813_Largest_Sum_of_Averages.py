'''

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
'''

class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        
        int n=A.size();
        int *a=new int[n+1];
        a[0]=0;
        for(int i=1;i<=n;i++){
            a[i]=a[i-1]+A[i-1];
            
        }
        
        //int *dp=new int[n];
        
       
        vector<vector<double>> dp(K,vector<double>(n,0.0));
        for(int i=0;i<K;i++){
            for(int j=0;j<n;j++){
                dp[i][j]=i==0?1.0*(a[j+1])/(j+1):dp[i-1][j];
                cout<<dp[i][j]<<endl;
                if(i>0){
                    for(int k=j-1;k>=0;k--){
                        //cout<<j-k;
                        dp[i][j]=max(dp[i][j],dp[i-1][k]+1.0*((a[j+1]-a[k+1]))/(j-k));
                    }
                }
                cout<<dp[i][j]<<endl;
            }
        }
        return dp[K-1][n-1];
        
    }
};
