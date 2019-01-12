'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        /*
        可以根据数组中数字的序号和元素进行匹配，通过交换位置的方式进行整理，使得数字尽量处于和本身数值相对应的序号上去，当发现第一个序         号和对应位上的数值不相等时，就得到了第一个缺失的正整数。
        
        1.只有满足索引范围的数组值我们才进行交换
        2.如果出现两个需要交换的位置上数值是一样的，就没必要换了
        */
        
        int n=nums.size();
        
        int i=0;
        while(i<n){
            if(nums[i]!=i+1 && nums[i]>=1 && nums[i]<=n&& nums[i]!=nums[nums[i]-1]){
                
                swap(nums[i],nums[nums[i]-1]);
                
            }else
                i++;
            
        }
        
       
        for(int i=0;i<n;i++){
            if(nums[i]!=i+1)
                return i+1;
        }
        return n+1;
        
        
        
    }
};