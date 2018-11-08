'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

 '''

 class Solution {
public:
    int numTrees(int n) {
        
        /*
        假设i为根节点，dp[i]为它的二叉树的数量。它的数量等于左子树的数量乘以右子树的数量。
        */
        
        vector<int> dp(n+1,0);
        dp[0]=1,dp[1]=1;
        for(int i=2;i<=n;i++){
            //遍历左子树的数量
            for(int j=0;j<i;j++)
                dp[i]+=dp[j]*dp[i-j-1];
            //count+=dp[i];
        }
        return dp[n];
    }
};