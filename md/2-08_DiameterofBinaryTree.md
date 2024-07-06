



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

# 3rd

- Odaさんコメント
isBalanced と height をペアにして返すようにすると、メモをしない再帰でも O(n) になります。

キャッシュするのも一つですが。

これ、友達を木の上の各ノードに立たせてですよ。電話させるんですよ。

で、マニュアルをばらまきます。
「木の高さいくら?」と聞かれた場合は、電話を保留状態にし、自分が null でない場合、部下全員に「木の高さいくら?」と電話をかけて、大きい方の数字に1を足してください。自分が null の場合は0です。保留を解除して返事をして下さい。

「バランスしている?」と聞かれた場合は、電話を保留状態にして、部下全員に「木の高さいくら?」と聞いて下さい。返事が返ってきたら、今度は部下全員に「バランスしている?」と聞いて下さい。


電話は、一回で済ませて下さい。isBalanced と height をペアにして返すようにすると、メモをしない再帰でも O(n) になります。


- fhiyoさんコメント
traverseという関数名でノードの深さが返ってくるのは少し違和感あるかもしれないです。
直径と深さの両方を返すようにしてもいいかも、と思いました。


⇒以上のコメントをもとにdiameterとheightをペアにして返すことによって計算量をO(n)にすることを検討

``` Python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_diameter_and_height(node) -> tuple[int, int]:
            if not node:
                return 0, 0
            left_diameter, left_height = get_diameter_and_height(node.left)
            right_diameter, right_height = get_diameter_and_height(node.right)
            diameter = max(left_diameter, right_diameter, left_height + right_height)
            height = max(left_height, right_height) + 1
            return diameter, height
        return get_diameter_and_height(root)[0]        
```