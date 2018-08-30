'''
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
 

Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)

'''


class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        
        /*
        列举所有的可能性,使用一个数组表示两个数字，然后遍历A中是否存在两者之和，然后更新这个数组；
       
        
        int n=A.size();
        set<int> a(A.begin(),A.end());
        int ans=INT_MIN;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                
                int nums[]={A[i],A[j]};
                
                int pos=0,count=2;
                
                while(a.find(nums[0]+nums[1])!=a.end()){
                    nums[pos]=nums[0]+nums[1];
                    pos=!pos;
                    count++;
                }
                ans=max(ans,count);
                
            }
        }
        if(ans<3) return 0;
        return ans;
         */
        
        /*
        使用动态规划，利用dp[i][j]表示以（i,j）结尾的斐波数的长度
        因此，dp[i][j]=dp[j-i][i]+1
        
        */
        
        int n=A.size();
        vector<vector<int>> dp(n,vector<int>(n,2));
        
        unordered_map<int,int> pos;
        
        for(int i=0;i<n;i++)
            pos[A[i]]=i;
        
        int ans=INT_MIN;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int pre=A[j]-A[i];
                if(pos.find(pre)!=pos.end() && pos[pre]<i){
                    dp[i][j]=dp[pos[pre]][i]+1;
                }
                
                ans=max(ans,dp[i][j]);
            }
        }
        return ans<3?0:ans;
        
    }
};