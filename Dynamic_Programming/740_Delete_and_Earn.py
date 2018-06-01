'''
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].

'''


class Solution {
public:
    /*
    int count;
    int get_result(vector<int> &nums,vector<bool> &isUsed,int n,int count){
        if(count==n)
            return 0;
        
        
        for(int i=0;i<n;i++){
            if(isUsed[i])
                continue;
            for(int j=0;j<n;j++){
                if(i==j)
                    continue;
                if(isUsed[j])
                    continue;
                if(nums[j]==nums[i]+1 || nums[j]==nums[i]-1){
                    isUsed[j]=true;
                    count++;
                }
                    
            
            }
            isUsed[i]=true;
            count++;
            return nums[i]+get_result(nums,isUsed,n,count);
            
            
        }
    }
    */
    int deleteAndEarn(vector<int>& nums) {
        
        /*
        int n=nums.size(),res=INT_MIN;
        if(n==0)
            return 0;
        for(int i=0;i<n;i++){
            int temp=0;
            count=1;
            vector<bool> isUsed(n,false);
            isUsed[i]=true;
            for(int j=0;j<n;j++){
                if(i==j)
                    continue;
                if(nums[j]==nums[i]+1 || nums[j]==nums[i]-1){
                    isUsed[j]=true;
                    count++;
                }
                    
                
            }
            temp=nums[i]+get_result(nums,isUsed,n,count);
            
            if(temp>res)
                res=temp;
            
            
        }
        return res;
        */
        
        /*
        子问题：f(0,i)
        每个子问题有两个选择：拿这个数字或者不拿这个数字
        填桶法
        */
        
        vector<int> dp(10001,0);
        vector<int> res(10001,0);
        int n=nums.size();
        
        for(int i=0;i<n;i++){
            res[nums[i]]+=nums[i];
        }
        dp[1]=res[1];
        for(int i=2;i<10001;i++){
            dp[i]=max(dp[i-1],res[i]+dp[i-2]);
        }
        return dp[10000];
        
        
        
        
    }
};