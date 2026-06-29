class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Узлы, которые нужно поменять местами
            first = current.next
            second = current.next.next

            # Меняем местами
            first.next = second.next
            second.next = first
            current.next = second

            # Переходим к следующей паре
            current = current.next.next

        return dummy.next
