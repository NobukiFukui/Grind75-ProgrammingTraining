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
