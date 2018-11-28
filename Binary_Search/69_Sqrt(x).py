'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

class Solution {
public:
    int mySqrt(int x) {
        
        if(x<2)
            return x;
        /*
        int res=1;
        while(pow(res+1,2)<=x)
            res++;
        return res;
        */
        
        int left=1,right=x;
        while(left<right){
            int mid=left+(right-left)/2;
            //防止溢出
            if(mid==x/mid) return mid;
            if(mid>x/mid) right=mid-1;
            else left=mid+1;
        }
        //cout<<right;
        if(right>x/right)
            return right-1;
        else
            return right;  
            
    }
};

