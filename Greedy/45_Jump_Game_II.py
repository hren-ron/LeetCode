'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.


'''

class Solution {
public:
    
    int jump(vector<int>& nums) {
        
        int n=nums.size();
        if(n==0 || n==1)
            return 0;
        int *jump=new int[n];
        for(int i=0;i<n;i++){
            jump[i]=-1;
        }
        jump[0]=0;
        for(int i=0;i<n;i++){
            int j=min(n-1,i+nums[i]);
            for(;j>i;j--){
                if(jump[j]!=-1)
                    break;
                jump[j]=jump[i]+1;
                if(j==n-1)
                    return jump[j];
            }
        }
        
        
    }
};
