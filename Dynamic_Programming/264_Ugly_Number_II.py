'''

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution {
public:
    int nthUglyNumber(int n) {
        /*
        int temp=1;
        
        int *a=new int[n];
        int m=n;
        while(n){
            //temp++;
            if(temp<=5){
                a[m-n]=temp;
                n--;
            }else{
                int t=INT_MAX;
                for(int i=0;i<m-n;i++){
                    for(int j=0;j<m-n;j++){
                        if(a[i]*a[j]<t && a[i]*a[j]>=temp)
                            t=a[i]*a[j];
                    }
                        
                }
                a[m-n]=temp;
                n--;
            }
            temp++;
        }
        return a[m-1];
        */
        
        vector<int> a(1,1);
        int i=0,j=0,k=0;
        while(a.size()<n){
            a.push_back(min(min(a[i]*2,a[j]*3),a[k]*5));
            if(a.back()==a[i]*2) ++i;
            if(a.back()==a[j]*3) ++j;
            if(a.back()==a[k]*5) ++k;
        }
        return a.back();
        
        
        
    }
};
