'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1=nums1.size();
        int len2=nums2.size();
        int len=len1+len2;
        if(len%2!=0)
            return find(nums1,0,len1,nums2,0,len2,len/2+1);
        else{
            //cout<<'e';
            return (find(nums1,0,len1,nums2,0,len2,len/2)+find(nums1,0,len1,nums2,0,len2,len/2+1))/2.0f;
        }
    }
    
    double find(vector<int> &nums1,int start1,int len1,vector<int> &nums2,int start2,int len2,int k){
        if(len1>len2)
            return find(nums2,start2,len2,nums1,start1,len1,k);
        if(len1==0)
            return nums2[start2+k-1];
        if(k==1)
            return min(nums1[start1],nums2[start2]);
        int p=min(len1,k/2);
        int q=k-p;
        
        if(nums1[start1+p-1]>nums2[start2+q-1])
            return find(nums1,start1,len1,nums2,start2+q,len2-q,k-q);
        else if(nums1[start1+p-1]<nums2[start2+q-1])
            return find(nums1,start1+p,len1-p,nums2,start2,len2,k-p);
        else
            return nums1[start1+p-1];
    }
};

