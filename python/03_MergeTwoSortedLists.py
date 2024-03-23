# ===============================================================
# (program) 03_MergeTwoSortedLists
# WaveAlchemist
# Description: 
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
#
# URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
# ===============================================================
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# %%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = [1,2,4]
ln1 = ListNode(list1[0])
print(ln1.next)

#%% 1st
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         if list1 and list2:
#             i = 0
#             mergedlist = []
#             while list2:
#                 for num in list1:
#                     if num >= list2[i]:
#                         list1.insert(list1.index(num),list2[i])
#                         list2.remove(list2[i])
#             i += 1
#         elif not list1:
#             return list2
#         elif not list2:
#             return list1
#         else:
#             return []




        

# list1 = [1,2,4]
# list2 = [1,3,4]
# Solution.mergeTwoLists(list1,list2)


# %% 2nd

# class Solution:
#     def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next

# list1 = ListNode(1,ListNode(2,ListNode(4)))
# list2 = ListNode(1,ListNode(2,ListNode(3)))
# Solution.mergeTwoLists([],list1,list2)


# %% 3rd

class Solution:
    def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
        cur = sentinel = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2            
        return sentinel.next

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(2,ListNode(3)))
Solution.mergeTwoLists([],list1,list2)