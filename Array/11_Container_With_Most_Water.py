'''


Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution {
public:
    int maxArea(vector<int>& height) {
        
        /*
        暴力搜索
        
        
        int res=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i==j)
                    continue;
                res=max(res,min(height[i],height[j])*abs(i-j));
            }
        }
        return res;
        */
        
        /*
        
        使用两个指针表示两个边，面积是由短边决定的，因此，从短边的这个位置每次移动一个指针，虽然宽度会降低，但是短边会变成较长的边，可能会得到更大的面积。
        */
        int n=height.size();
        if(n<2) return 0;
        int left=0,right=n-1,res=0;
        
        while(left<right){
            res=max(res,min(height[left],height[right])*(right-left));
            
            if(height[left]<height[right])
                left++;
            else
                right--;
        }
        return res;
    }
};
