class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    from typing import Optional
    def MergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy 
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 
                list1 = list1.next 
            else: 
                current.next = list2 
                list2 = list2.next 
            current = current.next 
        if list1:
            current.next = list1 
        else:
            current.next = list2 
        return dummy.next 

# Runtime 0 ms, Beats 100 %
# Memoru 17.65 MB, Beats 18.79 %
def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    merged_list = solution.MergeTwoLists(list1, list2)
    while merged_list:
        print(merged_list.val, end=" ")
        merged_list = merged_list.next

if __name__ == '__main__':
    main()
