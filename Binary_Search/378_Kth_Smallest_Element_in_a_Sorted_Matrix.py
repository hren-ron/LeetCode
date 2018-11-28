'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
'''


class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        
        /*
        将left取最小值, right取最大值，然后每次扫描整个数组查找小于(left+right)/2的元素个数，如果此个数小于k，则将left值变为               mid+1，否则right = mid,因为不同行之间可能不是递增的。
        */
        
        if(matrix.empty()) return -1;
        int n=matrix.size();
        
        int left=matrix[0][0],right=matrix.back().back();
        
        while(left<right){
            int mid=left+(right-left)/2,count=0;
            
            for(int i=0;i<n;i++)
                count+=upper_bound(matrix[i].begin(),matrix[i].end(),mid)-matrix[i].begin();
            if(count<k)
                left=mid+1;
            else
                right=mid;
        }
        return left;
        
    }
};