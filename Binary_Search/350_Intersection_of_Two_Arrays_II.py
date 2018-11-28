
'''

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        /*
        1.暴力搜索，每次搜到了就删除该元素
        
        int n=nums1.size(),m=nums2.size();
        
        vector<int> res;
        
        for(int i=0;i<n;i++)
            
            for(int j=0;j<nums2.size();j++)
                if(nums1[i]==nums2[j]){
                    res.push_back(nums2[j]);
                    nums2.erase(nums2.begin()+j);
                    break;
                }
        return res;
        */
        
        /*
        2.对于nums1建立一个哈希表,然后遍历nums2
        
        int n=nums1.size(),m=nums2.size();
        
        vector<int> res;
        unordered_map<int,int> hash;
        
        for(int i=0;i<n;i++)
            hash[nums1[i]]++;
        for(int j=0;j<m;j++){
            if(hash.count(nums2[j]) && hash[nums2[j]]>0){
                res.push_back(nums2[j]);
                hash[nums2[j]]--;
            }
        }
        return res;
        
        
        */
        /*
        3.对于两个数组排序，然后使用双指针；如果相等，加入；否则小的指针前移
        */
        
        int n=nums1.size(),m=nums2.size();
        
        vector<int> res;
        
        sort(nums1.begin(),nums1.end());
        
        sort(nums2.begin(),nums2.end());
        int i=0,j=0;
        while(i<n && j<m){
            if(nums1[i]==nums2[j]){
                res.push_back(nums1[i]);
                i++;
                j++;
                
            }else if(nums1[i]<nums2[j])
                i++;
            else
                j++;
        }
        return res;
    }
};
