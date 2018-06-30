'''

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''


class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        
        int n=nums.size();
        if(n<2)
            return false;
        if(k==0){
            for(int i=0;i<n;i++){
                if(nums[i]==k && nums[i+1]==0)
                    return true;
            }
            return false;
            
        }
            
        /*
        for(int i=2;i<=n;i++){
            for(int j=0;j<n-i+1;j++){
                int t=i,ans=0;
                while(t){
                    t--;
                    ans+=nums[j+t];
                }
                if(ans%k==0)
                    return true;
            }
        }
        */
        
        for(int i=0;i<n;i++){
            int sum=nums[i];
            for(int j=i+1;j<n;j++){
                sum+=nums[j];
                if(k!=0 && sum%k==0)
                    return true;
            }
        }
        /*(1)
        map<int, int> m = new map<int, int>();
        m.put(0,-1);
        int sum=0;
        for(int i=0;i<n;i++){
            sum=sum+nums[i];
            if(k!=0)
                sum=sum%k;
            int temp=m.get(sum);
            if(temp){
                if(i-temp>1)
                    return true;
            }else{
                m.put(sum,i);
            }
        }
        */
        return false;
        
    }
};