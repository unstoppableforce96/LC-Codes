# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # Find middle
        slow = fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse from middle
        prev = None
        while slow != None:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Compare
        left = head
        right = prev
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True