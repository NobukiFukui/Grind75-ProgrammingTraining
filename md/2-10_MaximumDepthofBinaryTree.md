# 2-10_MaximumDepthofBinaryTree
Author: WaveAlchemist
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# 1st-2nd
Diameter of Binary Treeで実装した再帰を思い出して解答したが
return 0のところを1としてしまい不正解になってしまった
後でDiameter of Binary Treeを見て修正した

``` Python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        depth = max(left_depth, right_depth) + 1
        return depth
```
# 3rd
discord上のほかの人が解答されたコードを見て自分で再構築
- https://github.com/fhiyo/leetcode/pull/23/files
    - 幅優先探索　 BFS
    - 深さ優先探索 DFS
- https://discordapp.com/channels/1084280443945353267/1227073733844406343/1236695050902048899
    - 

``` Python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def append_node(nodes, node):
            if not node:
                return
            nodes.append(node)
        if not root:
            return 0
        depth = 0
        nodes = [root]
        while nodes:
            next_depth_nodes = []
            for node in nodes:
                append_node(next_depth_nodes, node.left)
                append_node(next_depth_nodes, node.right)
            nodes = next_depth_nodes
            depth += 1
        return depth
```

``` Python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        nodes_with_depth = [(root, 1)]
        while nodes_with_depth:
            node, depth = nodes_with_depth.pop()
            max_depth = max(depth, max_depth)
            if node.left:
                nodes_with_depth.append((node.left, depth + 1))
            if node.right:
                nodes_with_depth.append((node.right, depth + 1))
        return max_depth
```

