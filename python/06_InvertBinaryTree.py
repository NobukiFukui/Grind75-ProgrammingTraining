# ===============================================================
# (program) 06_InvertBinaryTree
# WaveAlchemist
# Description: 
# Given the root of a binary tree, invert the tree, and return its root.
# URL: https://leetcode.com/problems/invert-binary-tree/description/
# 
# ===============================================================

# %% 1st 
# Copy of https://leetcode.com/problems/invert-binary-tree/solutions/3199238/0-ms-simplest-solution-full-explanation-c-python3/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: #Base Case
            return root
        self.invertTree(root.left) #Call the left subtree
        self.invertTree(root.right)  #Call the right subtree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root # Return the root

tree = TreeNode(2, TreeNode(1), TreeNode(3))
solution = Solution()
tree2 = solution.invertTree(tree)
print(tree2)

# %%
