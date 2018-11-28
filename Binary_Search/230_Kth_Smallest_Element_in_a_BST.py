'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
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
    int kthSmallest(TreeNode* root, int k) {
        /*
        1.中序遍历得到有序的序列
        
        vector<int > res;
        
        inOrder(root,res);
        return res[k-1];
        */
        
        /*
        看root左子树有多少点，如果正好等于k-1, 则返回root.val, 如果小于k-1, 就在root右子树中找       第k-leftSum-1小的点值, 若果大于k-1, 就在左子树中找第k小的点值。
        
        int l=count(root->left);
        if(l==k-1) 
            return root->val;
        else if(l>k-1)
            return kthSmallest(root->left,k);
        else
            return kthSmallest(root->right,k-l-1);
            
        
        */
        
        /*
        非递归的版本
        */
        
        stack<TreeNode *> stk;
        
        while(root!=NULL || !stk.empty()){
            if(root!=NULL){
                stk.push(root);
                //cout<<root->val<<endl;
                //cout<<stk<<endl;
                root=root->left;
                
            }else{
                //cout<<stk.top();
                root=stk.top();
                stk.pop();
                k--;
                if(k==0) return root->val;
                root=root->right;
            }
        }
        
        
        
        
        
    }
    int count(TreeNode *root){
        if(root==NULL) return 0;
        return 1+count(root->left)+count(root->right);
    }
    
    void inOrder(TreeNode *root,vector<int> &res){
        if(root==NULL) return;
        inOrder(root->left,res);
        res.push_back(root->val);
        inOrder(root->right,res);
    }
};
