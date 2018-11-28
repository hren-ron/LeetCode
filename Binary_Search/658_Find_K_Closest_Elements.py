'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

'''


class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        /*
        
        1.距离最远的必定出现在两端，因此每次去掉一个数字，知道数组的长度等于k
        
        
        vector<int> res=arr;
        while(res.size()>k){
            
            if(x-res.front()<=res.back()-x)
                res.pop_back();
            else
                res.erase(res.begin());
                
        }
        return res;
        
        */
        
        /*
        2.每次比较的是mid位置和x的距离跟mid+k跟x的距离，如果x-arr[mid]>arr[mid+k]-x,那么left=mid+1,
        */
        
        int left=0,right=arr.size()-k;
        
        while(left<right){
            int mid=left+(right-left)/2;
            
            if(x-arr[mid]>arr[mid+k]-x) left=mid+1;
            else right=mid;
            
        }
        
        return vector<int> (arr.begin()+left,arr.begin()+left+k);
        
    }
};