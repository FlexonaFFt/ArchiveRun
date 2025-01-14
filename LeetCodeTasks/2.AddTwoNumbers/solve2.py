class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, list1, list2):
        def reverse_linked_list(head):
            prev, current = None, head 
            while current:
                next_node = current.next
                current.next = prev 
                prev = current 
                current = next_node 
            return prev 

        def linked_list_to_number(head):
            num_str, current = '', head 
            while current:
                num_str += str(current.val)
                current = current.next 
            return int(num_str)

        def number_to_linked_list(number):
            dummy, current = ListNode(), dummy 
            for char in str(number):
                current.next = ListNode(int(char))
                current = current.next
            return dummy.next 

        
        # Обработка решения 
        reversed_list1 = reverse_linked_list(list1)
        reversed_list2 = reverse_linked_list(list2)
        num1 = linked_list_to_number(reversed_list1)
        num2 = linked_list_to_number(reversed_list2)
        sum_result = num1 + num2 
        result_list = number_to_linked_list(sum_result)
        return result_list

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print(result)

if __name__ == '__main__':
    main()
