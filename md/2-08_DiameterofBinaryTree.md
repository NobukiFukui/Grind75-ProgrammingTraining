



# 1st

nodeの下にある右および左のtreeから深度（left_diameter, right_diameter）を再帰にて取得を考えたが動きませんでした．
``` Python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterOfBinaryTreeHelper(tree, left_diameter, right_diameter):
            
            if not tree:
                return left_diameter + right_diameter
            if tree.left:            
               left_diameter += 1
               diameterOfBinaryTreeHelper(tree.left, left_diameter, right_diameter)
            if tree.right:
                right_diameter += 1
                diameterOfBinaryTreeHelper(tree.right, left_diameter, right_diameter)
    
        return diameterOfBinaryTreeHelper(root, 0, 0)

```

# 2nd

kitakenさんを参考に再構築
https://github.com/Kitaken0107/GrindEasy/pull/17/commits/6ba7ac9c546ffe4571f3e45175c94aa8a130b20c
自分で何も見ずに再構築はできましたが，まだ理解が浅い気がします

``` Python
class Solution:
    def __init__(self):
        self.diameter = 0
    def traverse(self, node):
        if not node:
            return 0
        # Recursively find the height of left and right subtrees
        left_height = self.traverse(node.left)
        right_height = self.traverse(node.right)
        # Update the diameter with the sum of left and right heights
        self.diameter = max(self.diameter, left_height + right_height)
        # Return the height of the current node
        return max(left_height, right_height) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.traverse(root)
        return self.diameter
```