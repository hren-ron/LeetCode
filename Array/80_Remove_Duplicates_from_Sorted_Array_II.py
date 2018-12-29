'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        /*
        使用两个指针，一个指针指向新的数组插入的位置，一个指针指向原数组的位置。count用于统计出现的次数
        
        声明两个指针first和second，first代表新的数组中最后一个元素的下一个位置，用来表示插入新元素的位置。

second表示当前遍历的元素位置，用来跟前一个元素比较是否相同，然后还需要一个计数器count，来统计相同元素出现的个数。

如果元素出现相同，然后观察此时count大小，如果之前只出现1次，则按正常处理（将当前遍历的元素插入到新位置，由first指出），然后count+1；
        */
        
        int n=nums.size();
        if(n<=2) return n;
        int first=1,second=1,count=1;
        
       while (second<nums.size())
        {
            if (nums[second-1] == nums[second] )
            {
                if (count<2)
                {
                    nums[first++] = nums[second];
                    count++;
                }
            }
            else
            {
                count = 1;
                nums[first++] = nums[second];
            }
            second++;
        }
        return first;
        
    }
};