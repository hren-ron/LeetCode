'''

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''


class Solution {
public:
    int divide(int dividend, int divisor) {
        
        
       
       
        if(dividend==-2147483648 && divisor==-1) return 2147483647;
        
        
        bool flag;
       
        if((dividend>0 &&divisor>0) || (dividend<0 && divisor<0))
            flag=true;
        else
            flag=false;
        
        long long n=labs(dividend);
        long long m=labs(divisor);
        int res=0;
        //cout<<m<<n<<endl;
        while(m<=n){
            
            long long temp=m;
            int count=1;
            
            while(n>=(temp<<1)){
                temp<<=1;
                count<<=1;
            }
            n-=temp;
            res+=count;
            //cout<<n<<endl;
        }
        if(flag)
            return res;
        else
            return(0-res);
       
         
    }
};
