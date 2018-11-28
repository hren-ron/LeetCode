'''


Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
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
    int countNodes(TreeNode* root) {
        /*
        广度优先搜索
        if(root==NULL)
            return 0;
        queue<TreeNode*> q;
        q.push(root);
        int count=0;
        while(!q.empty()){
            TreeNode* temp=q.front();
            q.pop();
            count++;
            if(temp->left!=NULL)
                q.push(temp->left);
            if(temp->right!=NULL)
                q.push(temp->right);
        }
        return count;
        */
        /*
        首先计算出二叉树的最左侧分支和最右侧分支的层数，如果二者相等，则整个二叉树是满二叉树；若不          相等，则递归的计算左右子树的节点数，总结点数=左子树节点数+右子树节点数+1。


        
        if(root==NULL) return 0;
        
        int ll=0,rr=0;
        TreeNode *l=root,*r=root;
        while(l){
            ll++;
            l=l->left;
        }
        while(r){
            rr++;
            r=r->right;
        }
        
        if(ll==rr)
            return ((1<<ll)-1);
        else{
            return (1+countNodes(root->left)+countNodes(root->right));
        }
        
        */
        
        /*
        利用二分法，
        寻找根节点的右子节点的最左后代节点，或者寻找根节点的左节点的最右后代节点，就可以找到底层叶         子的中间节点。
        
        对于根节点，如果在最底层能够找到它的右子节点的最左后代节点，说明根节点的左子树是完全二叉           树，这个时候我们需要检查该最左后代节点的后面一段，只需要深入一层到根节点的右子节点，继续寻·         找它的右子节点的最左后代节点即可，否则，说明左子树的高度比右子树高，并且根节点的右子树的最         底一层是满的，如果不是满的，这个树就不是完全二叉树。因此，深入一层到根节点的左子节点，继续         寻找它的右子节点的最左后代节点，如此下去。

        */
        
        if(root==NULL) return 0;
        
        int ll=get_leftmost(root->left);
        
        int rr=get_leftmost(root->right);
        int count=1;
        
        if(ll==rr){
            count+=(1<<ll)-1;
            count+=countNodes(root->right);
        }else{
            count+=(1<<rr)-1;
            count+=countNodes(root->left);
        }
        return count;
        
        
    }
    
    int get_leftmost(TreeNode *root){
        int count=0;
        while(root){
            count++;
            root=root->left;
        }
        return count;
    }
};
