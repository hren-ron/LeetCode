'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
        /*
        1.先从后往前找使得nums[i]>nums[i-1],后面的是降序，所以下一个排列必定是在i-1这个位置上；
        2.在i-1之后的位置上，找到刚刚大于nums[i-1]的数字，即nums[j].交换nums[i-1]和nums[j]
        3.此时在i-1的位置之后，仍然是降序的，因为我们找的是之前大于原来的nums[i-1]最小的数字，因此，原来是降序现在也是降序的
        4.由于要找的下一个排序，因此i-1之后的位置上应该是升序，所以要倒置后面的序列
        */
        
        int n=nums.size();
        
        int i=n-2;
        while(i>=0 && nums[i]>=nums[i+1]) --i;
        
        if(i>=0){
            int j=n-1;
            while(j>=0 && nums[j]<=nums[i]) --j;
            
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
        }
        
        int start=i+1,end=n-1;
        while(start<end){
            int temp=nums[start];
            nums[start]=nums[end];
            nums[end]=temp;
            start++;
            end--;
        }
        
    }
};