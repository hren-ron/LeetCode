'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

class Solution {
public:
    /*
    bool canjump(int position,vector<int>& nums){
        
        if(position==nums.size()-1)
            return true;
        int n=position+nums[position]<=nums.size()-1?position+nums[position]:nums.size()-1;
        for(int i=position+1;i<=n;i++){
            if(canjump(i,nums))
                return true;
        }
        return(false); 
    }
    */
    bool canJump(vector<int>& nums) {
        //return canjump(0,nums);
        int last=nums.size()-1;
        for(int i=nums.size()-2;i>=0;i--){
            if(i+nums[i]>=last)
                last=i;
        }
        return(last==0);
    }
};
