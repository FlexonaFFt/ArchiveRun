class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    from typing import Optional
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Runtime 0 ms, 100 %
# Memory 17.82 mb, 39.47 %
# Функции для тестирования (Не относятся к решению)
def list_to_linkedlist(lst):
    head = ListNode(0)
    current = head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return head.next

def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

def main():
    solution = Solution()
    head = list_to_linkedlist([1, 1, 2])
    result_head = solution.deleteDuplicates(head)
    result_list = linkedlist_to_list(result_head)
    print(result_list)

main()
