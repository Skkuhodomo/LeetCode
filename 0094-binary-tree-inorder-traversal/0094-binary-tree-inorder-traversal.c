/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int  cnt = 0;


int test(struct TreeNode* root, int* returnSize){
    if(!root){return 0;}
    cnt++;
    test(root->left, returnSize);
    test(root->right, returnSize);
    return cnt;
}

void fill(struct TreeNode* root, int* ret){
    if(!root){return;}
    fill(root->left, ret);
    ret[cnt++] = root->val;//store the element in inorder
    fill(root->right, ret);
    return;
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* ret =NULL;
    cnt = test(root, returnSize);//find out how many elements are there in this tree
    ret = (int*)calloc(cnt,sizeof(int));//initial return array with size
    cnt = 0;//reset the cnt variable for later use
    fill(root, ret);//fill the result array
    *returnSize = cnt;//fill return size
    cnt = 0;//reset the cnt variable

    return ret;
}