# ===============================================================
# (program) 11_BalancedBinaryTree
# WaveAlchemist
# Description: Given a binary tree, determine if it is height-balanced
#
# URL: https://leetcode.com/problems/balanced-binary-tree/description/
# ===============================================================

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0 
    def Height(self, root):
        # Base case
        if not root: return 0
        # Height of left and right subtrees
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        # If diff of height of left and right subtree >= 2 -> return -1
        if leftheight == -1 or rightheight == -1 or abs(leftheight-rightheight) >= 2:
            return -1
        # Return height of tree
        return max(leftheight, rightheight) + 1 

