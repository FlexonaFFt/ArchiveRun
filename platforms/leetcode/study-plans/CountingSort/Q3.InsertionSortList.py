# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(float('-inf'))
        curr = head

        while curr:
            next_node = curr.next  # запомним следующий
            # найдём позицию для вставки
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # вставка curr между prev и prev.next
            curr.next = prev.next
            prev.next = curr
            # дальше
            curr = next_node

        return dummy.next

