'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution {
public:
    int trap(vector<int>& height) {
        
        /*
        记录下每个位置的左右两边的最高的数，然后计算每个位置的容水量
        */
        
        int n=height.size(),ans=0,mx=0;
        
        if(n<=2) return ans;
        vector<int> left(n,0);
        
       
        for(int i=0;i<n;i++){
            left[i]=mx;
            
            mx=max(mx,height[i]);
        }
        mx=0;
        for(int i=n-1;i>=0;i--){
            left[i]=min(mx,left[i]);
            mx=max(height[i],mx);
            if(left[i]-height[i]>0)
                ans+=left[i]-height[i];
        }
        return ans;
        
        
    }
};
