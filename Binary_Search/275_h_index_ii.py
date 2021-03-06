'''

Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
'''

class Solution {
public:
    int hIndex(vector<int>& citations) {
        
        
        /*
        二分搜索：
        当前位置为i,如果n-i>nums[i],说明引用量大于 nums[i]的论文比较多，因此h-index应该在后面；
        否则就在前面找；
        */
        int n=citations.size();
        
        int left=0,right=n-1;
        while(left<=right){
            int mid=(left+right)/2;
            
            if(n-mid==citations[mid])
                return citations[mid];
            if(n-mid<citations[mid])
                right=mid-1;
            else
                left=mid+1;
        }
        return n-left;
    }
};