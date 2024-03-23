# ===============================================================
# (program) 06_InvertBinaryTree
# WaveAlchemist
# Description: 
# Given the root of a binary tree, invert the tree, and return its root.
# URL: https://leetcode.com/problems/invert-binary-tree/description/
# 
# ===============================================================

# %% 1st
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        


