'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
'''

class Solution {
public:
    bool canCross(vector<int>& stones) {
        /*
        我们用变量k表示当前石头，然后开始遍历剩余的石头，对于遍历到的石头i，我们来找到刚好能跳到i上的石头k，如果i和k的距离大于青蛙在k上的弹跳力+1，则说明         青蛙在k上到不了i，则k自增1。我们从k遍历到i，如果青蛙能从中间某个石头上跳到i上，我们更新石头i上的弹跳力和最大弹跳力。这样当循环完成后，我们只要           检查最后一个石头上青蛙的最大弹跳力是否大于0即可
        
        unordered_map<int,unordered_set<int>> jumps;
        
        int n=stones.size();
        vector<int> dp(n,0);
        
        jumps[0].insert(0);
        
        int k=0;
        for(int i=1;i<n;i++){
            
            while(dp[k]+1<stones[i]-stones[k]) ++k;
            
            
            for(int j=k;j<i;j++){
                
                int temp=stones[i]-stones[j];
                
                if(jumps[j].count(temp-1) || jumps[j].count(temp) || jumps[j].count(temp+1)){
                    jumps[i].insert(temp);
                    dp[i]=max(dp[i],temp);
                }
            
            }
        }
        return dp[n-1]>0;
        */
        
        /*
        使用map纪录青蛙在当前的石头上所能跳的步数，如果最后能到达最后一块石头，返回true
        */
        
        map<int,set<int>> jumps;
        
        int n=stones.size();
        set<int> t;
        for(int i=0;i<n;i++)
            jumps.insert(pair<int,set<int>>(stones[i],t));
        
        jumps[0].insert(1);
        
        for(int i=0;i<n;i++){
            
            
            for(auto step : jumps[stones[i]]){
                
                int reach=stones[i]+step;
                if(reach==stones[n-1])
                    return true;
                
                if(jumps.find(reach)!=jumps.end()){
                    jumps[reach].insert(step);
                    jumps[reach].insert(step+1);
                    if(step-1>0) jumps[reach].insert(step-1);
                }
                
            }
        }
        return false;
        
        
    }
};


