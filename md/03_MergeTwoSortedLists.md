# 03_MergeTwosortedLists
Author: WaveAlchemist  
URL: https://leetcode.com/problems/merge-two-sorted-lists/

# 1st
方針：
list1の要素をwhileループを用いて参照し，list2の各要素と比較する
list1 = [1,2,4], list2 = [1,3,4]
とする場合
list1[0] と list2[0]を比較して並べ替える
結果：
エラー⇒ListNodeの使い方が違う
TypeError: 'ListNode' object is not iterable
    for num in list1:
Line 13 in mergeTwoLists (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().mergeTwoLists(param_1, param_2)
Line 52 in _driver (Solution.py)
    _driver()
Line 63 in <module> (Solution.py)

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            i = 0
            mergedlist = []
            while list2:
                for num in list1:
                    if num >= list2[i]:
                        list1.insert(list1.index(num),list2[i])
                        list2.remove(list2[i])
            i += 1
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            return []

```

# 2nd 
方針：
https://leetcode.com/problems/merge-two-sorted-lists/solutions/1826693/python3-merging-explained/
を参照
そもそもlist1とlist2が既にListNodeであるということが理解できていなった（つまり，ただのListだと勘違い）
空のListNodeを作成して，list1とlist2の各要素で大きいほうを空のListNodeに格納する
結果：
成功したが，少し疑問が残る

return dummy.nextではListNodeの全体（つまり[1,1,2,3,4]みたいな形）で帰ってきているのか？
list1.nextでは一つの値しか返ってきていないような


``` Python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curNode = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curNode.next = list1
                list1, curNode = list1.next, list1
            else:
                curNode.next = list2
                list2, curNode = list2.next, list2
        if list1 or list2:
            if list1:
                curNode.next = list1
            else:
                curNode.next = list2
        return dummy.next


```