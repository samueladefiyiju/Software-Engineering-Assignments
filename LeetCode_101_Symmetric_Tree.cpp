class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        
        if (root == NULL){
            return true; 
        }
        else{
            
            return isMirror(root->left, root->right); 
        }
        
    }
    
    bool isMirror(TreeNode* left, TreeNode* right){
        
        if (left == NULL && right == NULL){
            return true; 
        }
        
        else if (left == NULL || right == NULL) {
            
            return false; 
            
        }
        
        else if (left->val != right->val){ 
        
            return false; 
        }
        
        else{
            
            return isMirror(left->left, right->right) && isMirror(left->right, right->left); 
        }
        
    }
};
