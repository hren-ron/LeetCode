'''

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
 

Note:

1 <= target <= 10000.
'''


class Solution {
public:
    
    int get_bit(int target){
        
        int count=0;
        while(target>0){
            count++;
            target=target>>1;
        }
        return count;
    }
    int racecar(int target) {
        
        /*
        因为速度乘以2，如果一直是A的话，position=1+2+4+8+....
        因此，如果target=2^k-1的话，走k步就可以到；
        但是如果2^(k-1)-1<i<2^k-1,可以有两种选择：
        1.走到2^(k-1)-1，然后停下来使用R，然后走A,走j个A的话，因为是反方向，就会离target越来越远。然后R停止,相当于回到原始状态速度为1；
        2.走到2^k-1,然后停下来，利用之前已经计算好的结果
        */
        
        vector<int> dp(target+3,INT_MAX);
        dp[0]=0,dp[1]=1,dp[2]=4;
        
        for(int i=3;i<=target;i++){
            int k=get_bit(i);
            //cout<<k<<endl;
            if((1<<k)-1==i){
                dp[i]=k;
                
            }else{
                for(int j=0;j<k-1;j++){
                    dp[i]=min(dp[i],k-1+j+2+dp[i-((1<<(k-1))-1)+(1<<j)-1]);
                    //cout<<((1<<(k-1))-1)<<i-(1<<(k-1)-1)+(1<<j)-1<<endl;
                }
                //如果target距离2^k-1更近，那么更新dp[target]
                
                if((1<<k)-1-i<i){
                    dp[i]=min(dp[i],dp[(1<<k)-1-i]+k+1);
                    //cout<<(1<<k)-1-i;
                }
                    
               
            }
            
            
        }
        //cout<<dp[target];
        return dp[target];
        
        
        
        
    }
};
