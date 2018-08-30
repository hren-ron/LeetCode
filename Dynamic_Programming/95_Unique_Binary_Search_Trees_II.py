'''

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        
        /*
        1. 每一次都在一个范围内随机选取一个结点作为根。 
        2. 每选取一个结点作为根，就把树切分成左右两个子树，直至该结点左右子树为空。
        */
        vector<TreeNode *> ans;
        if(n==0)
            return ans; 
        return generate(1,n);
        //return 0;
    }
    
    vector<TreeNode*> generate(int left,int right){
        /*
        vector<TreeNode*> res;
        
        if(i>j){
            res.push_back(NULL);
            return res;
        }
        
        for(int k=i;k<=j;k++){
            vector<TreeNode*> left=generate(i,k-1);
            vector<TreeNode*> right=generate(k+1,j);
            
            for(TreeNode* l:left){
                for(TreeNode* r:right){
                    TreeNode* root=new TreeNode(i);
                    root->left=l;
                    root->right=r;
                    res.push_back(root);
            }
        }
        }
        return res;
        */
        
        if (left > right) return vector<TreeNode *>(1, NULL);
        vector<TreeNode *> ans;
        for (int i = left; i <= right; i++) {
            vector<TreeNode *> leftTree = generate(left, i-1);
            vector<TreeNode *> rightTree = generate(i+1, right);
            for (int l = 0; l < leftTree.size(); l++) {
                for (int r = 0; r < rightTree.size(); r++) {
                    TreeNode* root = new TreeNode(i);
                    root->left = leftTree[l];
                    root->right = rightTree[r];
                    ans.push_back(root);
                }
            }
        }
        return ans;
        
        
    }
};
