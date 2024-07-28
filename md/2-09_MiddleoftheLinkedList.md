# 2-09_MiddleoftheLinkedList
Author: WaveAlchemist
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

# 1st
初見では以下の方針で解答
- nodeを最後まで（Noneになるまで）進める
- 最後まで進んだらその時何番目か（node_count）を返す
- int(node_count / 2 + 1)番目まで最初からnodeを進める
- nodeの数を計算する関数と希望するnode数nodeを進める関数を作成
解答時間は12min39sでした
思いついたアルゴリズムがこれだけだったのでこれで提出しましたが，無駄なことをやっているような気がしています．

```  Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def checkNodeNumber(node, node_count):
            while node.next:
                node = node.next
                node_count += 1
            return node_count
        def proceedNode(node, end_node):
            node_count = 1
            while node.next and node_count:
                node = node.next
                node_count += 1
                if node_count == end_node:
                    return node
            return node
        max_node_count = checkNodeNumber(head, 1)
        middle_node_count = int(max_node_count / 2 + 1)
        return proceedNode(head, middle_node_count)
```

# 2nd
LeetCodeのSolutionsを参照
Linked List Cycleで出てきたfastとslowを用いる方法を実装
fast.nextがNoneになった時点でfastはmiddle nodeにいるということに留意

``` Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
```

# 3rd
レビューのコメントをもとに再度構築しました（解法は1stのものをベースにしています）

- int(max_node_count / 2 + 1) -> max_node_count // 2 + 1
- node_count = 1に1-indexedというコメントを付与
- checkNodeNumber -> check_node_number, proceedNode -> proceed_node
- proceed_node内部でnodeを進めるごとにnum_proceedを1ずつ減らすという方法を実装

check_node_numberでnodeの数を数える場合

```Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def check_node_number(node):
            node_count = 1 # 1-indexed
            while node.next:
                node = node.next
                node_count += 1
            return node_count

        def proceed_node(node, num_proceed):
            while node.next:
                node = node.next
                num_proceed -= 1 
                if num_proceed == 0:
                    return node
            return node

        max_node_count = check_node_number(head)
        middle_node_count = max_node_count // 2 + 1
        return proceed_node(head, middle_node_count - 1)

```

check_node_numberをcheck_middle_node_numberとし，進めるべきnode数（つまり真ん中のnode数）を計算する場合
return node_count // 2として，proceed_nodeに代入するのはmiddle_node_countでいいのかも
（ただ，関数の名前的にはノードの数ということになるので，感覚としては現状がいい気もする。
つまり，真ん中のノードの数とノードを進める回数は違うということ）

``` Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def check_middle_node_number(node):
            node_count = 1 # 1-indexed
            while node.next:
                node = node.next
                node_count += 1
            return node_count // 2 + 1
        
        def proceed_node(node, num_proceed):
            while node.next:
                node = node.next
                num_proceed -= 1
                if num_proceed == 0:
                    return node
            return node
        
        middle_node_count = check_middle_node_number(head)
        print(middle_node_count)
        return proceed_node(head, middle_node_count - 1)
```

関数を使わない方法も試してみる
思ったよりスッキリかけた気がします．nodeを進めるときのwhile文はfor文で書いてもいいかもしれません．

``` Python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        node_count = 1 # 1-indexed
        # check node number
        while node.next:
            node = node.next
            node_count += 1
        # check node number to be proceeded
        num_proceed = node_count // 2
        # proceed node
        node = head
        for proceed in range(num_proceed, 0, -1):
            node = node.next
        return node
```