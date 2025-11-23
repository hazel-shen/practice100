# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LeetCode would do it for you.
def list_to_linkedlist(input_list):
    dummy = ListNode(0)
    current = dummy
    
    for val in input_list:
        current.next = ListNode(val)
        current = current.next
        
    return dummy.next

# For debugging.
def print_linkedlist(head):
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals))

def reverseList(head):
    prev = None
    current = head
    while current is not None:
        # reverse process
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        current = head
        carry = 0
        l1_reversed = reverseList(l1)
        l2_reversed = reverseList(l2)
        while l1_reversed is not None or l2_reversed is not None or carry != 0:
            x = l1_reversed.val if l1_reversed is not None else 0
            y = l2_reversed.val if l2_reversed is not None else 0
            summary = x + y + carry
            carry = summary // 10 # / is float division
            digit = summary % 10 
            new_node = ListNode(digit)

            current.next = new_node
            current = new_node

            if l1_reversed is not None:
                l1_reversed = l1_reversed.next
            if l2_reversed is not None:
                l2_reversed = l2_reversed.next
                
                
        return reverseList(head.next)

            
s = Solution()
l1_node = list_to_linkedlist([7, 2, 4, 3])
l2_node = list_to_linkedlist([5, 6, 4])
result = s.addTwoNumbers(l1_node, l2_node)
print_linkedlist(result)