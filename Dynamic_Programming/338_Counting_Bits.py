'''

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''


class Solution {
public:
    vector<int> countBits(int num) {
        
        vector<int> dp(num+1,0);
        
        /*
        直接计算每个数字的1的数量
        
        for(int i=0;i<=num;i++){
            int x=i,count=0;
            while(x!=0){
                if(x%2==1)
                    count++;
                x=x>>1;
            }
            dp[i]=count;
                
            
        }
        return dp;
        */
        
        /*
        计算n的时候，如果n%2==0,那么dp[n]=dp[n/2]
        否则，dp[n]=dp[n/2]+1;
        
        
        
        for(int i=1;i<=num;i++){
            if(i%2==0)
                dp[i]=dp[i/2];
            else
                dp[i]=dp[i/2]+1;
        }
        */
        
        /*
        利用了i&(i - 1)， 这个本来是用来判断一个数是否是2的指数的快捷方法，比如8，二进制位1000, 那么8&(8-1)为0，只要为0就是2的指数
        
        
        for(int i=1;i<=num;i++){
            dp[i]=dp[i &(i-1)]+1;
        }
        */
        
        /*
        除去前两个数字0个1，从2开始，2和3，是[21, 22)区间的，值为1和2。而4到7属于[22, 23)区间的，值为1,2,2,3，前半部分1和2和上一区间相同，2和3是上面的         基  础上每个数字加1。再看8到15，属于[23, 24)区间的，同样满足上述规律
        
        */
        
        
        dp[1]=1;
        
        int i=2,k=2;
        
        while(i<=num){
            
            for(i=pow(2,k-1);i<pow(2,k);i++){
                if(i>num)
                    break;
                
                int t=(pow(2,k)-pow(2,k-1))/2;
                
                if(i<pow(2,k-1)+t)
                    dp[i]=dp[i-t];
                else
                    dp[i]=dp[i-t]+1;
                
            }
            k++;
        }
        
        return dp;
        
    }
};
