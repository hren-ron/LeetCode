'''
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is guaranteed to be less than 231-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        
        
        int n=A.size();
        if(n<3)
            return 0;
        /*
        并不是产生连续的等差序列，所以当一个新的元素A[i]出现时，并不能简单地计算它和前一个元素的差值。因此需要遍历之前的元素，计算差值。
        把差值相同的合并，因此动态规划需要二维数据，dp[i][diff];
        建立等差数列的差值和当前位置之前差值相同的数字个数之间的映射
        */
        /*
        int count=0;
        for(int k=1;k<=n/2;k++){
            vector<int> dp(n,0);
            for(int i=2;i<n;i++){
                if(i-2*k>=0){
                    if(A[i]-A[i-k]==A[i-k]-A[i-2*k]){
                         dp[i]=dp[i-k]+1;
                        count+=dp[i];
                        cout<<i<<k<<endl;
                    }
                       
                    
                }
            }
        }
        return count;
        */
        int count=0;
        vector<unordered_map<int, int>> dp(n);
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
               long delta = (long)A[i] - A[j];
                if (delta > INT_MAX || delta < INT_MIN) continue;
                int diff = (int)delta;
                ++dp[i][diff];
                if(dp[j].count(diff)){
                    count+=dp[j][diff];
                    dp[i][diff]+=dp[j][diff];
                }
            }
        }
        return count;
    }
};
