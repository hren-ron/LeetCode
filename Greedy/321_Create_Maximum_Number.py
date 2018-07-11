'''
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
'''

class Solution {
public:
    
    vector<int> get_number(vector<int> &nums,int k){
        vector<int> res;
        int n=nums.size();
        int m=n-k;
        
        for(int i=0;i<n;i++){
            while(m>0 && res.size() && res.back()<nums[i]){
                res.pop_back();
                m--;
            }
            res.push_back(nums[i]);
        }
        
        res.resize(k);
        return res;
    }
    
    vector<int> merge(vector<int> &nums1,vector<int> &nums2 ){
        vector<int> res;
        while (nums1.size() + nums2.size()) {
            vector<int> &tmp = nums1 > nums2 ? nums1 : nums2;
            res.push_back(tmp[0]);
            tmp.erase(tmp.begin());
        }
        return res;
        
    }
    
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        
        /*
        把该问题分解成两个子问题：分别从两个数组中抽取i个最大的元素，然后把这些元素合并在一起。
        */
        int m=nums1.size();
        int n=nums2.size();
        
        int *dp=new int[k];
        vector<int> res;
        for(int i=max(0,k-n);i<=k && i<=m;i++){
            vector<int> n1=get_number(nums1,i);
            vector<int> n2=get_number(nums2,k-i);
            vector<int> temp=merge(n1,n2);
            res=max(res,temp);
        }
        return res;
        
    }
};
