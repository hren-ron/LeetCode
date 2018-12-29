'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        
        /*
        从第一个元素开始，每次保留开始的元素的值，依次扫描后面的元素，如果有连续的就一直往后查找，直到 遇到不连续的，然后记录这段范围。直到遍历完所有的元素。
        */
        
        int n=nums.size();
        vector<string> res;
        if(n==0) return res;
        string temp;
        int start=0,end=0;
        for(int i=1;i<=n;i++){
            if(nums[i]==nums[i-1]+1)
                end=i;
            else{
                if(start==end){
                    temp=to_string(nums[start]);
                    //res.push_back(temp);
                }else{
                    temp=to_string(nums[start])+"->"+to_string(nums[end]);
                    
                }
                res.push_back(temp);
                
                if(i<n){
                    start=i;
                    end=i;
                }
            }
        }
        return res;
    }
};